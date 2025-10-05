#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REN'PY AUTO TRANSLATOR v6.0 - SIMPLIFIED
- Auto-detect all .rpy files in folder
- Process sequentially
- No protect/mapping (assuming pre-protected files)
"""

import re
import os
import time
import subprocess
import glob
from datetime import datetime

# ================ CONFIG ================
BAHASA_ASAL = "en"                  # Bahasa sumber
BAHASA_TUJUAN = "id"                # Bahasa target
JEDA_TERJEMAH = 0                  # Delay antar terjemahan (detik)
LOG_LEVEL = "ERROR"                 # Options: ALL, ERROR, SUMMARY
# ========================================

class RenPyAutoTranslator:
    def __init__(self, input_file):
        self.input_file = input_file
        self.output_file = self._generate_output_name()
        self.log_file = self._generate_log_name()
        self.total_lines = 0

        # Logging counters
        self.translation_stats = {
            'success': 0,
            'failed': 0,
            'empty_input': 0,
            'empty_output': 0,
            'errors': 0,
            'skipped_code': 0,
            'total_processed': 0
        }

        # Ren'Py keywords yang TIDAK boleh ditranslate
        self.skip_keywords = [
            'show ', 'scene ', 'play ', 'stop ', 'queue ',
            'image ', 'define ', 'transform ', 'screen ',
            'jump ', 'call ', 'return', 'menu:', 'if ',
            'python:', 'init ', 'label ', 'with ',
            'hide ', 'at ', 'as ', '$', 'pause',
            'nvl ', 'window ', 'voice ', 'sound ',
            'music ', 'audio ', 'renpy.', 'camera '
        ]

    def _generate_output_name(self):
        base, ext = os.path.splitext(self.input_file)
        return f"{base}_{BAHASA_TUJUAN}{ext}"

    def _generate_log_name(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.splitext(os.path.basename(self.input_file))[0]
        return f"log_{base_name}_{timestamp}.txt"

    def _init_log_file(self):
        if LOG_LEVEL == "SUMMARY":
            return
        with open(self.log_file, 'w', encoding='utf-8') as f:
            f.write("=== REN'PY TRANSLATION LOG v6.0 ===\n")
            f.write(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Input: {self.input_file}\n")
            f.write(f"Output: {self.output_file}\n")
            f.write(f"Bahasa: {BAHASA_ASAL} -> {BAHASA_TUJUAN}\n")
            f.write(f"Log Level: {LOG_LEVEL}\n")
            f.write("="*50 + "\n\n")

    def _log_translation(self, line_num, status, original_text, translated_text="", error_msg="", context=""):
        if LOG_LEVEL == "SUMMARY":
            return
        elif LOG_LEVEL == "ERROR" and status == "SUCCESS":
            return
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"BARIS {line_num} | STATUS: {status}\n")
            if context:
                f.write(f"CONTEXT: {context.strip()}\n")
            f.write(f"ASLI   : '{original_text}'\n")
            if translated_text and translated_text != original_text:
                f.write(f"HASIL  : '{translated_text}'\n")
            if error_msg:
                f.write(f"ERROR  : {error_msg}\n")
            f.write("-" * 40 + "\n\n")

    def _should_translate(self, line, text_match):
        """Check if text should be translated"""
        before_quote = line[:text_match.start()].strip().lower()

        # Skip jika ada keyword Ren'Py di awal baris
        for keyword in self.skip_keywords:
            if before_quote.startswith(keyword.lower()):
                return False

        # Skip jika ada tanda $ (Python code)
        if '$' in before_quote:
            return False

        # Skip jika di dalam menu options yang pendek
        if before_quote.endswith(':'):
            return False

        # Skip jika ini adalah block old
        if before_quote.endswith('old'):
            return False

        # Skip jika hanya path/filename
        text_content = text_match.group(1)
        if (text_content.endswith(('.png', '.jpg', '.mp3', '.ogg', '.wav')) or
            '/' in text_content or '\\' in text_content):
            return False

        return True

    def _do_translation(self, text):
        try:
            escaped_text = text.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")
            cmd = f'trans -brief -no-ansi {BAHASA_ASAL}:{BAHASA_TUJUAN} "{escaped_text}"'
            result = subprocess.run(
                cmd,
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=25,
                encoding='utf-8'
            )
            if result.returncode != 0:
                return None, result.stderr.strip() if result.stderr else "Translation command failed"
            translated = result.stdout.strip()
            if not translated:
                return None, "Empty translation result"
            return translated, None
        except subprocess.TimeoutExpired:
            return None, "Translation timeout (25s)"
        except Exception as e:
            return None, f"Unexpected error: {str(e)}"

    def _translate_text(self, text, line_num, context=""):
        self.translation_stats['total_processed'] += 1

        # Check empty input
        if not text or not text.strip():
            self.translation_stats['empty_input'] += 1
            self._log_translation(line_num, "EMPTY_INPUT", text, context=context)
            return text

        # Translate directly (no protection needed)
        translated, error = self._do_translation(text)

        if error:
            if "timeout" in error.lower():
                self.translation_stats['errors'] += 1
                self._log_translation(line_num, "TIMEOUT", text, error_msg=error, context=context)
            else:
                self.translation_stats['failed'] += 1
                self._log_translation(line_num, "FAILED", text, error_msg=error, context=context)
            return text

        if not translated:
            self.translation_stats['empty_output'] += 1
            self._log_translation(line_num, "EMPTY_OUTPUT", text, context=context)
            return text

        # Success
        self.translation_stats['success'] += 1
        self._log_translation(line_num, "SUCCESS", text, translated, context=context)
        return translated

    def _process_line(self, line, line_num):
        original_line = line.rstrip()
        
        # Skip empty lines, comments, and python code
        if (not original_line.strip() or 
            original_line.strip().startswith('#') or
            original_line.strip().startswith('$')):
            return line

        def smart_translate_match(match):
            text = match.group(1)
            # Check if should translate
            if not self._should_translate(original_line, match):
                self.translation_stats['skipped_code'] += 1
                self._log_translation(line_num, "SKIPPED_CODE", text, context=original_line)
                return f'"{text}"'
            
            # Translate
            translated = self._translate_text(text, line_num, context=original_line)
            return f'"{translated}"'

        # Process all quoted strings
        final_line = re.sub(r'"([^"]*)"', smart_translate_match, original_line)
        return final_line + '\n'

    def _write_summary_log(self):
        success_rate = (self.translation_stats['success'] / max(1, self.translation_stats['total_processed'])) * 100
        summary_text = f"""
{'='*60}
RINGKASAN TERJEMAHAN v6.0 - {os.path.basename(self.input_file)}
{'='*60}
✅ Berhasil ditranslate : {self.translation_stats['success']}
⏩ Skip (Ren'Py code)   : {self.translation_stats['skipped_code']}
❌ Gagal/Error         : {self.translation_stats['failed'] + self.translation_stats['errors']}
📝 Input kosong         : {self.translation_stats['empty_input']}
📄 Output kosong        : {self.translation_stats['empty_output']}
📊 Total diproses       : {self.translation_stats['total_processed']}
📋 Total baris file     : {self.total_lines}
🎯 Success Rate         : {success_rate:.1f}%
"""
        if LOG_LEVEL != "SUMMARY":
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(summary_text)
        print(summary_text)

    def _check_dependencies(self):
        try:
            result = subprocess.run("trans --version", shell=True, capture_output=True, timeout=5)
            if result.returncode != 0:
                print("❌ translate-shell tidak ditemukan!")
                print("📥 Install dengan: npm install -g translate-shell")
                return False
            return True
        except:
            print("❌ Error checking translate-shell dependency")
            return False

    def _validate_output(self):
        try:
            with open(self.output_file, 'r', encoding='utf-8') as f:
                content = f.read()
            issues = []
            quote_count = content.count('"')
            if quote_count % 2 != 0:
                issues.append("⚠️ Unmatched quotes detected")
            if content.count('{') != content.count('}'):
                issues.append("⚠️ Unmatched curly brackets")
            if content.count('[') != content.count(']'):
                issues.append("⚠️ Unmatched square brackets")
            
            if issues:
                print(f"\n🚨 SYNTAX WARNINGS:")
                for issue in issues:
                    print(f"   {issue}")
            else:
                print(f"\n✅ Syntax validation passed!")
        except Exception as e:
            print(f"\n⚠️ Could not validate syntax: {e}")

    def run(self):
        print(f"\n📂 Processing: {self.input_file}")
        if not os.path.exists(self.input_file):
            print(f"❌ File tidak ditemukan: {self.input_file}")
            return False
        
        if not self._check_dependencies():
            return False
            
        self._init_log_file()
        print(f"🚀 Memulai terjemahan...")
        print(f"⚙️ Mode: {LOG_LEVEL} logging | Delay: {JEDA_TERJEMAH}s")
        
        with open(self.input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        self.total_lines = len(lines)
        results = []
        start_time = time.time()
        
        for i, line in enumerate(lines, 1):
            processed = self._process_line(line, i)
            results.append(processed)
            percent = (i / self.total_lines) * 100
            success_rate = (self.translation_stats['success'] / max(1, self.translation_stats['total_processed'])) * 100
            elapsed = time.time() - start_time
            eta = (elapsed / i) * (self.total_lines - i) if i > 0 else 0
            print(f"\r📊 {percent:.1f}% | {i}/{self.total_lines} | Success: {success_rate:.0f}% | ETA: {eta:.0f}s", end='', flush=True)
            if JEDA_TERJEMAH > 0:
                time.sleep(JEDA_TERJEMAH)
        
        print()  # New line after progress
        
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.writelines(results)
            print(f"✅ Output saved: {self.output_file}")
        except Exception as e:
            print(f"❌ Error saving file: {e}")
            return False
        
        self._validate_output()
        self._write_summary_log()
        
        total_issues = (self.translation_stats['failed'] + 
                        self.translation_stats['errors'] + 
                        self.translation_stats['empty_output'])
        if total_issues > 0:
            print(f"⚠️ Ada {total_issues} teks bermasalah, cek log untuk detail!")
        else:
            print(f"🎉 Translation completed successfully!")
        
        return True


def main():
    print("\n" + "="*70)
    print("🎮 REN'PY AUTO TRANSLATOR v6.0 - SIMPLIFIED")
    print("🔍 Auto-detect .rpy files | Sequential processing")
    print("="*70)
    
    # Auto-detect all .rpy files in current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    rpy_files = glob.glob(os.path.join(current_dir, "*.rpy"))
    
    # Filter out already translated files (*_id.rpy)
    input_files = [f for f in rpy_files if not f.endswith(f"_{BAHASA_TUJUAN}.rpy")]
    
    if not input_files:
        print(f"\n❌ Tidak ada file .rpy yang ditemukan di folder ini!")
        print(f"📁 Current directory: {current_dir}")
        return
    
    print(f"\n📋 Ditemukan {len(input_files)} file .rpy:")
    for i, file in enumerate(input_files, 1):
        file_name = os.path.basename(file)
        file_size = os.path.getsize(file) / 1024  # KB
        with open(file, 'r', encoding='utf-8') as f:
            line_count = sum(1 for _ in f)
        print(f"   {i}. {file_name} ({line_count} lines, {file_size:.1f} KB)")
    
    # Process each file sequentially
    successful_files = []
    failed_files = []
    
    start_time = time.time()
    
    for i, input_file in enumerate(input_files, 1):
        print(f"\n{'='*70}")
        print(f"📁 FILE {i}/{len(input_files)}")
        print(f"{'='*70}")
        
        translator = RenPyAutoTranslator(input_file)
        success = translator.run()
        
        if success:
            successful_files.append(input_file)
        else:
            failed_files.append(input_file)
    
    total_time = time.time() - start_time
    
    # Final summary
    print(f"\n" + "="*70)
    print("📊 RINGKASAN AKHIR")
    print("="*70)
    print(f"✅ Berhasil : {len(successful_files)}/{len(input_files)} file")
    print(f"❌ Gagal    : {len(failed_files)} file")
    print(f"⏱️ Total    : {total_time/60:.1f} menit")
    
    if successful_files:
        print(f"\n🎉 File berhasil ditranslate:")
        for file in successful_files:
            output_name = os.path.splitext(os.path.basename(file))[0] + f"_{BAHASA_TUJUAN}.rpy"
            print(f"   ✅ {os.path.basename(file)} → {output_name}")
    
    if failed_files:
        print(f"\n❌ File gagal:")
        for file in failed_files:
            print(f"   ❌ {os.path.basename(file)}")
    
    print(f"\n✨ Selesai! Semua file telah diproses.")


if __name__ == "__main__":
    main()
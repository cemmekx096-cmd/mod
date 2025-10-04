#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REMOTE ORCHESTRATOR v1.0
Parallel translation orchestrator with Telegram notifications
"""

import os
import re
import shutil
import subprocess
import threading
import time
import requests
from datetime import datetime
from pathlib import Path

# ================ CONFIG ================
NAMA_SCRIPT_TRANSLATE = 'tran.py'
TOKEN_BOT_TELE = '7732517146:AAFxfT074Ma8kzWPWFXZgTR978hCAat-c0U'
TOKEN_CHAT_ID = '7121031492'
# ========================================

class TelegramNotifier:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.enabled = bot_token != 'your_bot_token_here' and chat_id != 'your_chat_id_here'
        
    def send(self, message):
        """Send message to Telegram"""
        if not self.enabled:
            print(f"[TELEGRAM DISABLED] {message}")
            return
            
        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            data = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            response = requests.post(url, data=data, timeout=10)
            if response.status_code != 200:
                print(f"⚠️ Telegram send failed: {response.text}")
        except Exception as e:
            print(f"❌ Telegram error: {e}")


class WorkerMonitor:
    def __init__(self, worker_id, folder_path, script_path, notifier):
        self.worker_id = worker_id
        self.folder_path = folder_path
        self.folder_name = os.path.basename(folder_path)
        self.script_path = script_path
        self.notifier = notifier
        
        self.files_processed = []
        self.files_failed = []
        self.is_running = False
        self.is_completed = False
        self.start_time = None
        self.end_time = None
        self.process = None
        
    def run(self):
        """Run translation script in worker folder"""
        self.is_running = True
        self.start_time = time.time()
        
        print(f"[Worker {self.worker_id}] Starting in folder: {self.folder_name}")
        self.notifier.send(f"⚙️ <b>[Worker {self.worker_id}]</b> Memulai proses di folder <code>{self.folder_name}</code>")
        
        try:
            # Run script in worker folder
            self.process = subprocess.Popen(
                ['python3', self.script_path],
                cwd=self.folder_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                bufsize=1,
                universal_newlines=True
            )
            
            # Monitor stdout in real-time
            for line in self.process.stdout:
                line = line.strip()
                if not line:
                    continue
                    
                print(f"[Worker {self.worker_id}] {line}")
                
                # Detect file completion
                if "✅ Output saved:" in line or "Output saved:" in line:
                    # Extract filename
                    match = re.search(r'([^\s/\\]+\.rpy)', line)
                    if match:
                        filename = match.group(1)
                        self.files_processed.append(filename)
                        self.notifier.send(
                            f"✅ <b>[Worker {self.worker_id}]</b> Berhasil: <code>{filename}</code>"
                        )
                
                # Detect errors
                elif "❌" in line or "ERROR" in line or "Error" in line:
                    # Try to extract filename
                    match = re.search(r'([^\s/\\]+\.rpy)', line)
                    if match:
                        filename = match.group(1)
                        self.files_failed.append(filename)
                        self.notifier.send(
                            f"❌ <b>[Worker {self.worker_id}]</b> ERROR: <code>{filename}</code>\n{line}"
                        )
            
            # Wait for process to complete
            self.process.wait()
            
            self.is_running = False
            self.is_completed = True
            self.end_time = time.time()
            
            duration = (self.end_time - self.start_time) / 60
            
            summary = f"""🎉 <b>[Worker {self.worker_id}] SELESAI</b>

📁 Folder: <code>{self.folder_name}</code>
✅ Berhasil: {len(self.files_processed)} files
❌ Gagal: {len(self.files_failed)} files
⏱️ Waktu: {duration:.1f} menit"""

            if self.files_failed:
                summary += f"\n\n⚠️ <b>File gagal:</b>\n"
                for f in self.files_failed:
                    summary += f"• <code>{f}</code>\n"
            
            self.notifier.send(summary)
            print(f"[Worker {self.worker_id}] Completed in {duration:.1f} minutes")
            
        except Exception as e:
            self.is_running = False
            self.is_completed = True
            error_msg = f"❌ <b>[Worker {self.worker_id}]</b> CRASH: {str(e)}"
            self.notifier.send(error_msg)
            print(f"[Worker {self.worker_id}] Exception: {e}")


class RemoteOrchestrator:
    def __init__(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.translate_script = os.path.join(self.script_dir, NAMA_SCRIPT_TRANSLATE)
        self.notifier = TelegramNotifier(TOKEN_BOT_TELE, TOKEN_CHAT_ID)
        self.workers = []
        self.start_time = None
        
    def find_worker_folders(self):
        """Find all subfolders containing numbers"""
        folders = []
        
        for item in os.listdir(self.script_dir):
            item_path = os.path.join(self.script_dir, item)
            
            # Skip if not directory
            if not os.path.isdir(item_path):
                continue
            
            # Skip hidden folders
            if item.startswith('.'):
                continue
            
            # Check if folder name contains number
            if re.search(r'\d+', item):
                folders.append(item_path)
        
        # Sort by number in folder name
        def extract_number(path):
            match = re.search(r'(\d+)', os.path.basename(path))
            return int(match.group(1)) if match else 0
        
        folders.sort(key=extract_number)
        return folders
    
    def copy_script_to_folders(self, folders):
        """Copy translate script to all worker folders"""
        print("\n📄 Copying translate script to worker folders...")
        
        if not os.path.exists(self.translate_script):
            print(f"❌ Master script not found: {self.translate_script}")
            return False
        
        for folder in folders:
            dest_script = os.path.join(folder, NAMA_SCRIPT_TRANSLATE)
            try:
                shutil.copy2(self.translate_script, dest_script)
                print(f"   ✅ Copied to: {os.path.basename(folder)}/")
            except Exception as e:
                print(f"   ❌ Failed to copy to {os.path.basename(folder)}/: {e}")
                return False
        
        print("✅ All scripts copied successfully!\n")
        return True
    
    def count_input_files(self, folders):
        """Count total .rpy files in all folders"""
        total = 0
        for folder in folders:
            rpy_files = [f for f in os.listdir(folder) if f.endswith('.rpy') and not f.endswith('_id.rpy')]
            total += len(rpy_files)
        return total
    
    def run(self):
        """Main orchestrator execution"""
        print("\n" + "="*70)
        print("🎮 REMOTE ORCHESTRATOR v1.0")
        print("🚀 Parallel Translation with Telegram Notifications")
        print("="*70)
        
        # Find worker folders
        print("\n🔍 Scanning for worker folders...")
        worker_folders = self.find_worker_folders()
        
        if not worker_folders:
            print("❌ No worker folders found!")
            print("   Create subfolders with numbers: 1/, 2/, _1/, chunk_0/, etc.")
            return
        
        print(f"✅ Found {len(worker_folders)} worker folders:")
        for i, folder in enumerate(worker_folders, 1):
            folder_name = os.path.basename(folder)
            rpy_count = len([f for f in os.listdir(folder) if f.endswith('.rpy') and not f.endswith('_id.rpy')])
            print(f"   {i}. {folder_name}/ ({rpy_count} files)")
        
        total_files = self.count_input_files(worker_folders)
        print(f"\n📊 Total files to translate: {total_files}")
        
        # Copy script to folders
        if not self.copy_script_to_folders(worker_folders):
            print("❌ Failed to copy scripts. Aborting.")
            return
        
        # Send start notification
        self.start_time = time.time()
        start_msg = f"""🚀 <b>TRANSLATION STARTED</b>

👷 Workers: {len(worker_folders)} parallel
📁 Total files: {total_files}
⏰ Started: {datetime.now().strftime('%H:%M:%S')}"""
        
        self.notifier.send(start_msg)
        
        # Create workers
        print("="*70)
        print("🚀 Starting parallel workers...\n")
        
        threads = []
        for i, folder in enumerate(worker_folders, 1):
            script_path = os.path.join(folder, NAMA_SCRIPT_TRANSLATE)
            monitor = WorkerMonitor(i, folder, script_path, self.notifier)
            self.workers.append(monitor)
            
            # Start worker in thread
            thread = threading.Thread(target=monitor.run)
            thread.start()
            threads.append(thread)
            
            time.sleep(0.5)  # Stagger starts slightly
        
        # Wait for all workers to complete
        print("\n⏳ Waiting for all workers to complete...\n")
        for thread in threads:
            thread.join()
        
        # Calculate statistics
        total_time = (time.time() - self.start_time) / 60
        total_success = sum(len(w.files_processed) for w in self.workers)
        total_failed = sum(len(w.files_failed) for w in self.workers)
        
        # Final summary
        print("\n" + "="*70)
        print("📊 FINAL SUMMARY")
        print("="*70)
        
        summary_msg = f"""✅ <b>TRANSLATION COMPLETED!</b>

📊 <b>Statistics:</b>
• Total files: {total_files}
• Success: {total_success}
• Failed: {total_failed}
• Workers: {len(worker_folders)}
• Total time: {total_time:.1f} minutes

<b>Worker Details:</b>"""
        
        for worker in self.workers:
            duration = (worker.end_time - worker.start_time) / 60 if worker.end_time else 0
            summary_msg += f"\n• Worker {worker.worker_id}: {len(worker.files_processed)} files ({duration:.1f}m)"
        
        if total_failed > 0:
            summary_msg += f"\n\n⚠️ <b>Failed files: {total_failed}</b>"
            for worker in self.workers:
                if worker.files_failed:
                    summary_msg += f"\n• Worker {worker.worker_id}: {', '.join(worker.files_failed)}"
        
        summary_msg += f"\n\n🎯 <b>Next steps:</b>"
        summary_msg += f"\n1. Check output files (*_id.rpy)"
        summary_msg += f"\n2. Merge if needed"
        summary_msg += f"\n3. Compile & inject!"
        
        self.notifier.send(summary_msg)
        
        # Console summary
        print(f"\n✅ Total Success: {total_success}/{total_files}")
        print(f"❌ Total Failed: {total_failed}/{total_files}")
        print(f"⏱️ Total Time: {total_time:.1f} minutes")
        print(f"🚀 Average speed: {total_time/len(worker_folders):.1f} min/worker")
        
        if total_failed > 0:
            print(f"\n⚠️ WARNING: {total_failed} files failed!")
            print("Check logs for details.")
        else:
            print("\n🎉 All files translated successfully!")
        
        print("\n" + "="*70)


def main():
    orchestrator = RemoteOrchestrator()
    orchestrator.run()


if __name__ == "__main__":
    main()
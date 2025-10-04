import re
import os
from pathlib import Path

def process_translation_file(input_file, output_file):
    """
    Memproses file terjemahan dengan aturan:
    1. Ganti 'translate english' menjadi 'translate id'
    2. Hapus '# ' dari semua baris
    3. Skip baris yang setelah dihapus '#' hasilnya jadi 'nama_karakter ""'
    4. Auto-generate 'new' dari nilai 'old'
    5. Skip baris 'new ""' yang sudah ada di input
    """
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    output_lines = []
    skip_next_new = False
    
    for line in lines:
        # Rule 1: Ganti 'translate english' dengan 'translate id'
        if re.search(r'translate\s+english', line, re.IGNORECASE):
            output_lines.append(re.sub(r'translate\s+english', 'translate id', line, flags=re.IGNORECASE))
            skip_next_new = False
            continue
        
        # Rule 2 & 3: Hapus '# ' dan cek apakah hasilnya kosong
        if line.strip().startswith('#'):
            cleaned_line = re.sub(r'^(\s*)#\s+', r'\1', line)
            
            # Skip jika hasilnya 'nama ""'
            if re.match(r'^\s*\w+\s+""', cleaned_line):
                skip_next_new = False
                continue
            
            output_lines.append(cleaned_line)
            skip_next_new = False
            continue
        
        # Skip baris yang sudah berupa 'nama ""' (tanpa #)
        if re.match(r'^\s*\w+\s+""', line):
            skip_next_new = False
            continue
        
        # Skip baris yang hanya berisi ""
        if re.match(r'^\s*""\s*$', line):
            skip_next_new = False
            continue
        
        # Rule 4: Jika ada 'old "..."', auto-generate 'new "..."'
        old_match = re.search(r'old\s+"([^"]*)"', line)
        if old_match:
            output_lines.append(line)
            old_value = old_match.group(1)
            
            # Generate baris 'new' dengan nilai dari 'old'
            indent = len(line) - len(line.lstrip())
            new_line = ' ' * indent + f'new "{old_value}"\n'
            output_lines.append(new_line)
            
            skip_next_new = True
            continue
        
        # Rule 5: Skip baris 'new ""' jika sudah di-generate sebelumnya
        if skip_next_new and re.match(r'\s*new\s+""', line):
            skip_next_new = False
            continue
        
        # Default: tulis ulang baris seperti aslinya
        output_lines.append(line)
        skip_next_new = False
    
    # Buat folder output jika belum ada
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Tulis ke file output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

def process_all_rpy_files():
    """
    Memproses semua file .rpy di folder yang sama dengan script
    dan menyimpan hasilnya ke subfolder 'tl'
    """
    # Dapatkan folder tempat script berada
    script_dir = Path(__file__).parent
    
    # Cari semua file .rpy di folder script
    rpy_files = list(script_dir.glob('*.rpy'))
    
    if not rpy_files:
        print("❌ Tidak ada file .rpy ditemukan di folder ini!")
        return
    
    # Buat folder 'tl' jika belum ada
    tl_folder = script_dir / 'tl'
    tl_folder.mkdir(exist_ok=True)
    
    print(f"🔍 Ditemukan {len(rpy_files)} file .rpy")
    print(f"📁 Output akan disimpan ke: {tl_folder}\n")
    
    success_count = 0
    error_count = 0
    
    for rpy_file in rpy_files:
        try:
            # Tentukan path output
            output_file = tl_folder / rpy_file.name
            
            print(f"⚙️  Memproses: {rpy_file.name}...", end=' ')
            
            # Proses file
            process_translation_file(str(rpy_file), str(output_file))
            
            print(f"✓")
            success_count += 1
            
        except Exception as e:
            print(f"❌ Error: {e}")
            error_count += 1
    
    print(f"\n{'='*50}")
    print(f"✓ Berhasil: {success_count} file")
    if error_count > 0:
        print(f"❌ Gagal: {error_count} file")
    print(f"{'='*50}")

# Main program
if __name__ == "__main__":
    print("="*50)
    print("  RENPY TRANSLATION FILE PROCESSOR")
    print("="*50)
    print()
    
    try:
        process_all_rpy_files()
    except Exception as e:
        print(f"❌ Error fatal: {e}")
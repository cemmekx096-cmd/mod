import os
import re
from pathlib import Path

class RenPyTool:
    def __init__(self):
        self.script_dir = Path.cwd()
    
    # ==================== MENU 1: MERGE & UNMERGE ====================
    
    def merge_files(self):
        """Gabungkan semua file .rpy jadi satu dengan marker"""
        rpy_files = sorted(self.script_dir.glob('*.rpy'))
        
        if not rpy_files:
            print("❌ Tidak ada file .rpy ditemukan!")
            return
        
        print(f"\n🔍 Ditemukan {len(rpy_files)} file .rpy:")
        for i, f in enumerate(rpy_files, 1):
            print(f"   {i}. {f.name}")
        
        output_name = input("\n📝 Nama file output (default: merged.rpy): ").strip()
        if not output_name:
            output_name = "merged.rpy"
        if not output_name.endswith('.rpy'):
            output_name += '.rpy'
        
        output_path = self.script_dir / output_name
        
        with open(output_path, 'w', encoding='utf-8') as outfile:
            for rpy_file in rpy_files:
                if rpy_file.name == output_name:
                    continue
                
                print(f"⚙️  Menggabungkan: {rpy_file.name}")
                
                outfile.write(f"#========== AWAL {rpy_file.name} ==========\n")
                
                with open(rpy_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    if not content.endswith('\n'):
                        outfile.write('\n')
                
                outfile.write(f"#========== AKHIR {rpy_file.name} ==========\n\n")
        
        print(f"\n✅ Berhasil! File digabung ke: {output_name}")
    
    def unmerge_files(self):
        """Pisahkan file yang sudah di-merge kembali ke file aslinya"""
        rpy_files = list(self.script_dir.glob('*.rpy'))
        
        if not rpy_files:
            print("❌ Tidak ada file .rpy ditemukan!")
            return
        
        print("\n📁 File .rpy yang tersedia:")
        for i, f in enumerate(rpy_files, 1):
            print(f"   {i}. {f.name}")
        
        choice = input("\n📝 Pilih nomor file yang ingin di-unmerge: ").strip()
        try:
            file_index = int(choice) - 1
            merged_file = rpy_files[file_index]
        except (ValueError, IndexError):
            print("❌ Pilihan tidak valid!")
            return
        
        with open(merged_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern untuk mendeteksi marker
        pattern = r'#========== AWAL (.+?) ==========\n(.*?)#========== AKHIR \1 ==========\n*'
        matches = re.findall(pattern, content, re.DOTALL)
        
        if not matches:
            print("❌ File tidak memiliki marker merge yang valid!")
            return
        
        output_dir = self.script_dir / 'unmerged'
        output_dir.mkdir(exist_ok=True)
        
        print(f"\n📂 Output akan disimpan ke folder: unmerged/\n")
        
        for filename, file_content in matches:
            output_path = output_dir / filename
            print(f"⚙️  Membuat: {filename}")
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(file_content)
        
        print(f"\n✅ Berhasil! {len(matches)} file dipulihkan ke folder unmerged/")
    
    # ==================== MENU 2: SPLIT & JOIN ====================
    
    def split_file(self):
        """Pecah file besar jadi beberapa part berdasarkan jumlah baris"""
        rpy_files = list(self.script_dir.glob('*.rpy'))
        
        if not rpy_files:
            print("❌ Tidak ada file .rpy ditemukan!")
            return
        
        print("\n📁 File .rpy yang tersedia:")
        for i, f in enumerate(rpy_files, 1):
            print(f"   {i}. {f.name}")
        
        choice = input("\n📝 Pilih nomor file yang ingin di-split: ").strip()
        try:
            file_index = int(choice) - 1
            target_file = rpy_files[file_index]
        except (ValueError, IndexError):
            print("❌ Pilihan tidak valid!")
            return
        
        lines_per_part = input("📝 Jumlah baris per part (default: 3000): ").strip()
        try:
            lines_per_part = int(lines_per_part) if lines_per_part else 3000
        except ValueError:
            print("❌ Input tidak valid! Menggunakan default 3000")
            lines_per_part = 3000
        
        with open(target_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        total_lines = len(lines)
        base_name = target_file.stem
        output_dir = self.script_dir / f'{base_name}_parts'
        output_dir.mkdir(exist_ok=True)
        
        print(f"\n📊 Total baris: {total_lines}")
        print(f"📂 Output akan disimpan ke folder: {output_dir.name}/\n")
        
        part_num = 1
        for i in range(0, total_lines, lines_per_part):
            part_lines = lines[i:i + lines_per_part]
            part_file = output_dir / f'{base_name}_part{part_num}.rpy'
            
            with open(part_file, 'w', encoding='utf-8') as f:
                f.writelines(part_lines)
            
            print(f"⚙️  Membuat: {part_file.name} ({len(part_lines)} baris)")
            part_num += 1
        
        print(f"\n✅ Berhasil! File dipecah menjadi {part_num - 1} part")
    
    def join_parts(self):
        """Gabungkan kembali file yang sudah di-split"""
        # Cari folder yang berisi parts
        part_folders = [d for d in self.script_dir.iterdir() if d.is_dir() and '_parts' in d.name]
        
        if not part_folders:
            print("❌ Tidak ada folder parts ditemukan!")
            return
        
        print("\n📁 Folder parts yang tersedia:")
        for i, folder in enumerate(part_folders, 1):
            print(f"   {i}. {folder.name}")
        
        choice = input("\n📝 Pilih nomor folder yang ingin di-join: ").strip()
        try:
            folder_index = int(choice) - 1
            parts_folder = part_folders[folder_index]
        except (ValueError, IndexError):
            print("❌ Pilihan tidak valid!")
            return
        
        # Cari semua file part
        part_files = sorted(parts_folder.glob('*_part*.rpy'), key=lambda x: int(re.search(r'part(\d+)', x.name).group(1)))
        
        if not part_files:
            print("❌ Tidak ada file part ditemukan!")
            return
        
        base_name = parts_folder.name.replace('_parts', '')
        output_file = self.script_dir / f'{base_name}_joined.rpy'
        
        print(f"\n🔍 Ditemukan {len(part_files)} part files\n")
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for part_file in part_files:
                print(f"⚙️  Menggabungkan: {part_file.name}")
                
                with open(part_file, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
        
        print(f"\n✅ Berhasil! File digabung ke: {output_file.name}")
    
    # ==================== MENU 3: SCAN & REPLACE ====================
    
    def scan_and_replace(self):
        """Scan pattern dan replace dengan angka, simpan mapping"""
        rpy_files = list(self.script_dir.glob('*.rpy'))
        
        if not rpy_files:
            print("❌ Tidak ada file .rpy ditemukan!")
            return
        
        print("\n📁 File .rpy yang tersedia:")
        for i, f in enumerate(rpy_files, 1):
            print(f"   {i}. {f.name}")
        
        choice = input("\n📝 Pilih nomor file yang ingin di-scan: ").strip()
        try:
            file_index = int(choice) - 1
            target_file = rpy_files[file_index]
        except (ValueError, IndexError):
            print("❌ Pilihan tidak valid!")
            return
        
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Dictionaries untuk menyimpan mapping
        tag_map = {}
        variable_map = {}
        string_map = {}
        
        tag_counter = 1
        var_counter = 1
        string_counter = 1
        
        # Pattern untuk mencari
        tags = re.findall(r'\{([^}]+)\}', content)
        variables = re.findall(r'\[([^\]]+)\]', content)
        strings = re.findall(r'<([^>]+)>', content)
        
        # Buat mapping untuk tags
        for tag in tags:
            full_tag = f"{{{tag}}}"
            if full_tag not in tag_map:
                tag_map[full_tag] = f"{{{tag_counter}}}"
                tag_counter += 1
        
        # Buat mapping untuk variables
        for var in variables:
            full_var = f"[{var}]"
            if full_var not in variable_map:
                variable_map[full_var] = f"[{var_counter}]"
                var_counter += 1
        
        # Buat mapping untuk strings
        for string in strings:
            full_string = f"<{string}>"
            if full_string not in string_map:
                string_map[full_string] = f"<{string_counter}>"
                string_counter += 1
        
        # Replace content
        new_content = content
        for original, replacement in tag_map.items():
            new_content = new_content.replace(original, replacement)
        for original, replacement in variable_map.items():
            new_content = new_content.replace(original, replacement)
        for original, replacement in string_map.items():
            new_content = new_content.replace(original, replacement)
        
        # Simpan file hasil replace
        output_file = self.script_dir / f'{target_file.stem}_replaced.rpy'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        # Simpan mapping ke file txt
        mapping_file = self.script_dir / f'{target_file.stem}_mapping.txt'
        with open(mapping_file, 'w', encoding='utf-8') as f:
            if tag_map:
                f.write("=== TAG MAPPING ===\n")
                for original, replacement in tag_map.items():
                    f.write(f"{replacement} = {original}\n")
                f.write("\n")
            
            if variable_map:
                f.write("=== VARIABLE MAPPING ===\n")
                for original, replacement in variable_map.items():
                    f.write(f"{replacement} = {original}\n")
                f.write("\n")
            
            if string_map:
                f.write("=== STRING MAPPING ===\n")
                for original, replacement in string_map.items():
                    f.write(f"{replacement} = {original}\n")
                f.write("\n")
        
        print(f"\n📊 Hasil scan:")
        print(f"   Tags: {len(tag_map)}")
        print(f"   Variables: {len(variable_map)}")
        print(f"   Strings: {len(string_map)}")
        print(f"\n✅ File hasil: {output_file.name}")
        print(f"✅ Mapping: {mapping_file.name}")
    
    def restore_from_mapping(self):
        """Restore file yang sudah di-replace kembali ke original menggunakan mapping file"""
        # Cari file _replaced.rpy
        replaced_files = list(self.script_dir.glob('*_replaced.rpy'))
        
        if not replaced_files:
            print("❌ Tidak ada file *_replaced.rpy ditemukan!")
            return
        
        print("\n📁 File yang bisa di-restore:")
        for i, f in enumerate(replaced_files, 1):
            print(f"   {i}. {f.name}")
        
        choice = input("\n📝 Pilih nomor file yang ingin di-restore: ").strip()
        try:
            file_index = int(choice) - 1
            replaced_file = replaced_files[file_index]
        except (ValueError, IndexError):
            print("❌ Pilihan tidak valid!")
            return
        
        # Cari file mapping yang sesuai
        base_name = replaced_file.stem.replace('_replaced', '')
        mapping_file = self.script_dir / f'{base_name}_mapping.txt'
        
        if not mapping_file.exists():
            print(f"❌ File mapping tidak ditemukan: {mapping_file.name}")
            return
        
        # Baca file yang akan di-restore
        with open(replaced_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse mapping file
        tag_map = {}
        variable_map = {}
        string_map = {}
        
        current_section = None
        
        with open(mapping_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                if line == "=== TAG MAPPING ===":
                    current_section = "tag"
                elif line == "=== VARIABLE MAPPING ===":
                    current_section = "variable"
                elif line == "=== STRING MAPPING ===":
                    current_section = "string"
                elif line and '=' in line and current_section:
                    # Parse line: {1} = {original_tag}
                    parts = line.split(' = ', 1)
                    if len(parts) == 2:
                        replacement = parts[0].strip()
                        original = parts[1].strip()
                        
                        if current_section == "tag":
                            tag_map[replacement] = original
                        elif current_section == "variable":
                            variable_map[replacement] = original
                        elif current_section == "string":
                            string_map[replacement] = original
        
        # Restore content (replace dari angka ke original)
        restored_content = content
        
        # Sort berdasarkan panjang untuk menghindari replace yang salah
        for replacement, original in sorted(tag_map.items(), key=lambda x: len(x[0]), reverse=True):
            restored_content = restored_content.replace(replacement, original)
        
        for replacement, original in sorted(variable_map.items(), key=lambda x: len(x[0]), reverse=True):
            restored_content = restored_content.replace(replacement, original)
        
        for replacement, original in sorted(string_map.items(), key=lambda x: len(x[0]), reverse=True):
            restored_content = restored_content.replace(replacement, original)
        
        # Simpan file hasil restore
        output_file = self.script_dir / f'{base_name}_restored.rpy'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(restored_content)
        
        print(f"\n📊 Hasil restore:")
        print(f"   Tags: {len(tag_map)}")
        print(f"   Variables: {len(variable_map)}")
        print(f"   Strings: {len(string_map)}")
        print(f"\n✅ File di-restore ke: {output_file.name}")
    
    # ==================== MAIN MENU ====================
    
    def run(self):
        """Menu utama"""
        while True:
            print("\n" + "="*50)
            print("     RENPY MULTI-FUNCTION TOOL")
            print("="*50)
            print("\n📋 MENU:")
            print("   1. Merge & Unmerge Files")
            print("   2. Split & Join Files")
            print("   3. Scan & Replace Patterns")
            print("   0. Exit")
            
            choice = input("\n➡️  Pilih menu: ").strip()
            
            if choice == '1':
                self.menu_merge_unmerge()
            elif choice == '2':
                self.menu_split_join()
            elif choice == '3':
                self.menu_scan_replace()
            elif choice == '0':
                print("\n👋 Terima kasih!")
                break
            else:
                print("\n❌ Pilihan tidak valid!")
    
    def menu_merge_unmerge(self):
        """Submenu untuk merge/unmerge"""
        print("\n--- MERGE & UNMERGE ---")
        print("   1. Merge files (Gabungkan)")
        print("   2. Unmerge files (Pisahkan)")
        print("   0. Kembali")
        
        choice = input("\n➡️  Pilih: ").strip()
        
        if choice == '1':
            self.merge_files()
        elif choice == '2':
            self.unmerge_files()
    
    def menu_split_join(self):
        """Submenu untuk split/join"""
        print("\n--- SPLIT & JOIN ---")
        print("   1. Split file (Pecah)")
        print("   2. Join parts (Gabungkan)")
        print("   0. Kembali")
        
        choice = input("\n➡️  Pilih: ").strip()
        
        if choice == '1':
            self.split_file()
        elif choice == '2':
            self.join_parts()
    
    def menu_scan_replace(self):
        """Submenu untuk scan/replace/restore"""
        print("\n--- SCAN & REPLACE ---")
        print("   1. Scan & Replace (variable → angka)")
        print("   2. Restore (angka → variable)")
        print("   0. Kembali")
        
        choice = input("\n➡️  Pilih: ").strip()
        
        if choice == '1':
            self.scan_and_replace()
        elif choice == '2':
            self.restore_from_mapping()

# Main program
if __name__ == "__main__":
    tool = RenPyTool()
    tool.run()
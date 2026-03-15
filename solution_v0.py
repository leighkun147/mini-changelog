# Öğrenci: Leykun Hailemichael Hagos
# Öğrenci Numarası: 9241478125
import sys
import datetime
import os

# Bu fonksiyon changelog.txt dosyasını oluşturarak sistemi başlatır.
def init():
    if os.path.exists("changelog.txt"):
        print("Error: Changelog already initialized.")
    else:
        f = open("changelog.txt", "w")
        f.close()
        print("Changelog initialized.")

# Bu fonksiyon yeni bir günlük girdisini dosyaya ekler.
def add_entry(type_name, description):
    if not os.path.exists("changelog.txt"):
        print("Error: Changelog not initialized. Run 'init' first.")
    else:
        f_read = open("changelog.txt", "r")
        content = f_read.read()
        f_read.close()
        
        # Benzersiz ID'yi döngü kullanmadan belirlemek için satır sayısını sayarız.
        new_id = str(content.count("\n") + 1)
        date_str = str(datetime.date.today())
        
        # Veri formatı: id|tarih|tip|açıklama
        entry = new_id + "|" + date_str + "|" + type_name + "|" + description + "\n"
        
        f_write = open("changelog.txt", "a")
        f_write.write(entry)
        f_write.close()
        print("Entry added.")

# Bu fonksiyon henüz tamamlanmamış komutlar için bilgi mesajı verir.
def future_feature():
    print("Command will be implemented in future weeks")

# Bu fonksiyon komut satırı argümanlarını çözer ve uygun işlevi çağırır.
def main(script_name, command=None, arg1=None, arg2=None, *extra):
    if command is None:
        print("Error: No command provided.")
    elif command == "init":
        init()
    elif command == "add":
        if arg1 is None or arg2 is None:
            print("Error: Missing arguments for 'add'.")
        else:
            add_entry(arg1, arg2)
    elif command == "list":
        future_feature()
    elif command == "search":
        future_feature()
    else:
        print("Error: Unknown command.")

if __name__ == "__main__":
    # [] kullanmaktan kaçınmak için sys.argv'yi fonksiyon parametrelerine açıyoruz.
    main(*sys.argv)

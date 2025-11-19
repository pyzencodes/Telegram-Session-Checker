import asyncio
import os
import glob
import sys
import shutil
from telethon import TelegramClient, errors

# ========= API BİLGİLERİN =========
API_ID = XXXX
API_HASH = "XXXXXX"

# ========= KLASÖRLER =========
SESSIONS_DIR = "./sessions"
GOOD_DIR = "./sessions_ok"
BAD_DIR = "./sessions_bad"

if sys.platform.startswith("win"):
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except Exception:
        pass


async def check_session(session_path: str):
    """
    .session dosyasını dener:
    - authorized ise GOOD_DIR'e
    - değilse BAD_DIR'e kopyalar
    """
    file_name = os.path.basename(session_path)
    base_name = os.path.splitext(file_name)[0]

    # Telethon, verilen isme .session ekler; o yüzden .session uzantısını atıp klasörle veriyoruz
    session_name_for_telethon = os.path.join(SESSIONS_DIR, base_name)

    print(f"\n🔹 Session deneniyor: {file_name}")

    client = TelegramClient(session_name_for_telethon, API_ID, API_HASH)

    try:
        await client.connect()

        if not await client.is_user_authorized():
            print(" ❌ Yetkisiz / giriş yok, BAD klasöre atıyorum.")
            dest = os.path.join(BAD_DIR, file_name)
        else:
            me = await client.get_me()
            print(f" ✅ Giriş başarılı: @{me.username} | id={me.id} | phone={me.phone}")
            dest = os.path.join(GOOD_DIR, file_name)

        # Hedef klasöre kopyala (varsa üzerine yaz)
        shutil.copy2(session_path, dest)

    except errors.ApiIdInvalidError:
        print(" ❌ API_ID / API_HASH uyumsuz, BAD klasöre atıyorum.")
        dest = os.path.join(BAD_DIR, file_name)
        shutil.copy2(session_path, dest)
    except Exception as e:
        print(f" ⚠️ Hata: {e} -> BAD klasöre atıyorum.")
        dest = os.path.join(BAD_DIR, file_name)
        try:
            shutil.copy2(session_path, dest)
        except Exception:
            pass
    finally:
        try:
            await client.disconnect()
        except Exception:
            pass


async def main():
    # klasörleri hazırla
    os.makedirs(SESSIONS_DIR, exist_ok=True)
    os.makedirs(GOOD_DIR, exist_ok=True)
    os.makedirs(BAD_DIR, exist_ok=True)

    session_files = glob.glob(os.path.join(SESSIONS_DIR, "*.session"))
    print(f"📁 Bulunan session sayısı: {len(session_files)}")

    if not session_files:
        print("⚠️ sessions klasöründe hiç .session yok.")
        return

    for i, session_path in enumerate(session_files, start=1):
        print(f"\n[{i}/{len(session_files)}]")
        await check_session(session_path)

    # Özet
    good_count = len(glob.glob(os.path.join(GOOD_DIR, "*.session")))
    bad_count = len(glob.glob(os.path.join(BAD_DIR, "*.session")))

    print("\n==============================")
    print(f"✅ Başarılı (sessions_ok): {good_count}")
    print(f"❌ Başarısız (sessions_bad): {bad_count}")
    print("==============================")
    print("Bitti. Artık erişebildiğimiz hesaplar 'sessions_ok' klasöründe.")


if __name__ == "__main__":
    asyncio.run(main())

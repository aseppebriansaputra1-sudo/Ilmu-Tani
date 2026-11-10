# Pustaka Tani (Android, 100% offline)

## Build APK lewat GitHub
1. Buat repo baru di GitHub, upload SELURUH isi folder ini (termasuk folder `.github` dan `scripts`).
2. Tab **Actions** -> **Build APK** -> **Run workflow** (juga jalan otomatis setiap push).
3. Setelah hijau, buka run tersebut, unduh artifact **PustakaTani-apk**, ekstrak, install `app-debug.apk`.

Saat build, font diunduh otomatis lalu dikemas ke dalam APK, jadi aplikasi tidak butuh internet sama sekali.
Aplikasi juga tidak meminta izin INTERNET.

## Update isi
Ganti `app/src/main/assets/index.html`, push, lalu unduh APK baru.

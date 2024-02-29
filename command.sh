#!/bin/bash


git pull

# Systemd xizmatlarini qayta boshlash
sudo systemctl daemon-reload

# Celery xizmatini qayta boshlash
sudo systemctl enable emaktab_beat
sudo systemctl start emaktab_beat
sudo systemctl restart emaktab_beat




# Celery beat xizmatini qayta boshlash (agar kerak bo'lsa)
sudo systemctl enable emaktab_beat
sudo systemctl start emaktab_beat
sudo systemctl restart emaktab_beat





# Telegram_ads.socket va telegram_ads.service xizmatlarini qayta boshlash
sudo systemctl restart emaktab.socket
sudo systemctl restart emaktab.service

# client.service xizmatini qayta boshlash (agar kerak bo'lsa)
#sudo systemctl restart client.service

# Nginx konfiguratsiyasini tekshirish va Nginx ni qayta boshlash
sudo nginx -t && sudo systemctl restart nginx



sudo systemctl status emaktab_beat
sudo systemctl status emaktab_worker
docker run -p 8080:80 -v/home/pi/project/html/:/usr/share/nginx/html -d --restart unless-stopped nginx

sudo crontab -e
sudo ps axjf
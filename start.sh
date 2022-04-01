echo "Cloning Repo...."
git clone https://github.com/godofanjal/Music-Player.git /Music-Player
cd /Music-Player
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py

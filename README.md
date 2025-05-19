# AI_motion
Text extraction, PLN and classification package

## 🔧 Step-by-Step: Get Reddit API Credentials

### 1. Create a Reddit account (if you don’t already have one):
Go to https://www.reddit.com/register

### 2. Go to Reddit's app preferences:
Visit https://www.reddit.com/prefs/apps

### 3. Scroll down to “Developed Applications”
Click “create another app...” or “create app”.

### 4. Fill in the form:

Creating app page:

![image](https://github.com/user-attachments/assets/59b07b1e-e684-4a07-b5dd-0f954ea53f0e)

Tutorial:

```bash
name: Any name you want for your app.

type: Choose “script” (for personal scripts, like bots).

description: (optional)

about url: Can be left blank.

redirect uri: Use http://localhost:8080 (you can also use this for development purposes).

permissions: Not needed unless you're requesting scopes manually.
```

### 5. Click “create app”

### 6. After Creating the App
You will see:

client_id: Right under the app name (a 14-character string).

client_secret: A long string under “secret”.

user_agent: A description string you create

## 🔧 Step-by-Step: Installing



### 2. Clone the repository and open your local directory:

```bash
git clone https://github.com/Franklinbrt/AI_motion.git
cd seu-repo
```

### 3. Tornar o script setup.sh executável
For Linux/macOS systems, you need to grant the script execution permission.
IMPORTANT: This permission is not automatically preserved by Git when cloning the repository.

```bash
chmod +x setup.sh
```

### 4. Run the installation script
After that, run the script to install the project dependencies:

```bash
./setup.sh
```

### 5. Running the project in a virtual environment (venv)
The setup.sh script already creates and activates a Python virtual environment to isolate the project's dependencies.

If you want to do it manually:

```bash
python3 -m venv venv
source venv/bin/activate    # Linux/macOS
# ou
venv\Scripts\activate       # Windows
pip install -r requirements.txt
```
## Usage

## 1.  Set up the config file with your Reddit credentials and the time period for text scraping

You can set it up config.yaml:

```yaml
# Configurações do usuário
user_settings:
    client_id:'ng3zVDs7S7Xj7soFTRemnA'
    client_secret:'uBOV7z9kSFSjRjcMdD0Zg1qZbKmRuA'
    user_agent:'YOUR_USER_AGENT' # don't need to change

#Períodos a serem selecionados pelo usuário
period:
    data_inicial:'2021-05-31'
    hora_inicial:'16:00:00'
    data_final:'2022-08-31'
    hora_final:'16:00:00'
```
## 2. Run the Data Scraper

Run the following commmand on the terminal in order to scrape posts from reddit.

```bash
python3 reddit_scrapping.py
```

## 🔧 Step-by-Step: Apply PLN preprocessing


## 🔧 Step-by-Step: Classify


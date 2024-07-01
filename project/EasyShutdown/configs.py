import json
# 语言字典
LANGUAGES = {
    "zh": {
        "title": "简易关机 v0.0.1 - 作者:L.W.Kevin0wvf",
        "buttons": {
            "language": "切换语言(zh/en)",
            "style": "切换UI风格样式",
            "shutdown": "关机",
            "sleep": "睡眠",
            "reboot": "重启"
        },
        "events": {
            "on_closing": {
                "title": "退出",
                "content": "您想要退出吗？"
            }
        }
    },
    "en": {
        "title": "Easy Shutdown v0.0.1 - Author:L.W.Kevin0wvf",
        "buttons": {
            "language": "Toggle the language(zh/en)",
            "style": "Toggle the UI style",
            "shutdown": "Shutdown",
            "sleep": "Sleep",
            "reboot": "Reboot"
        },
        "events": {
            "on_closing": {
                "title": "Quit",
                "content": "Do you want to quit?"
            }
        }
    }
}

# UI风格样式
STYLES = {
    "default": {
        "fg": "#000000",
        "bg": "#f0f0f0"
    },
    "dark": {
        "fg": "#ffffff",
        "bg": "#202020"
    }
}

try:
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        # 当前语言
        current_language = config["language"]
        # 当前UI风格样式
        current_style = config["style"]
except FileNotFoundError:
    config = {"language": "zh", "style": "default"}
    # 添加config配置文件
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)
    # 当前语言
    current_language = config["language"]
    # 当前UI风格样式
    current_style = config["style"]

import json
# 语言字典
LANGUAGES = {
    "zh": {
        "title": "人民币发送 v0.0.1 - 作者:L.W.Kevin0wvf",
        "buttons": {
            "language": "切换语言(zh/en)",
            "style": "切换UI风格样式",
            "send": "发送"
        },
        "events": {
            "on_closing": {
                "title": "退出",
                "content": "您想要退出吗？"
            },
            "on_send": {
                "title": "发送人民币配置",
                "search_tips": "🔍搜索：",
                "confirm": "搜索",
                "refresh": "刷新",
                "money_tips": "💴钱数：",
                "send": "发送",
                "repeat": {
                    "title": "发送",
                    "content": "请勿打开多个发送配置窗口"
                }
            }
        }
    },
    "en": {
        "title": "RMB Send v0.0.1 - Author:L.W.Kevin0wvf",
        "buttons": {
            "language": "Toggle the language(zh/en)",
            "style": "Toggle the UI style",
            "send": "Send"
        },
        "events": {
            "on_closing": {
                "title": "Quit",
                "content": "Do you want to quit?"
            },
            "on_send": {
                "title": "Send RMB configs",
                "search_tips": "🔍Search:",
                "confirm": "Search",
                "refresh": "Refresh",
                "money_tips": "💴Amount of money:",
                "send": "Send",
                "repeat": {
                    "title": "Send",
                    "content": "Do not open more than one send configuration window"
                }
            }
        }
    }
}

# UI风格样式
STYLES = {
    "default": {
        "fg": "#000000",
        "bg": "#f0f0f0",
        "ibg": "#000000"
    },
    "dark": {
        "fg": "#ffffff",
        "bg": "#202020",
        "ibg": "#ffffff"
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

inputing = False
par = [100, 50, 20, 10, 5, 1]

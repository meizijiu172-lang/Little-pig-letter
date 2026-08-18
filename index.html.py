import json
import os
import webbrowser

# ==================== 1. 自定义情书内容与背景图片 ====================
RECIPIENT_NAME = "小猪"
YOUR_NAME = "你的宝宝"
DATE_TEXT = "2026年8月19日"

BACKGROUND_IMAGE = "book.jpg"
ENVELOPE_TIP = "开启"

LOVE_LETTER_CONTENT = [
    "是谁想到你",
    "嘴角就不自觉上扬",
    "是谁日思夜想",
    "期待与你相见",
    "失去你消息的我",
    "在分隔空间寻找存在",
    "用爱的光把虚拟分开",
    "撕破夜幕的阻碍",
    "光线穿越天罩的掩盖",
    "跟踪心跳的节拍现在",
    "站在城市中",
    "寂寞电波穿梭闪烁",
    "期待联络",
    "寻找你的全部线索",
    "Pretty Boy回答回答",
    "是你在喂喂喂吗",
    "送你的Radar Radar",
    "感应我的方向吧",
    "Pretty Boy回复加快",
    "Answer me tonight tonight it's tonight",
    "Pretty Boy留言等待",
    "Please tell me alright alright it's alright",
    "接收我的爱",
]
# ====================================================================


def generate_envelope_html_large_font():
  cleaned_content = [text.strip() for text in LOVE_LETTER_CONTENT]
  paragraphs_js = json.dumps(cleaned_content, ensure_ascii=False)

  html_code = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>给{RECIPIENT_NAME.strip()}的信</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        html, body {{
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }}
        body {{
            background-image: url('{BACKGROUND_IMAGE}');
            background-repeat: no-repeat;
            background-position: center center;
            background-size: cover;
            background-attachment: fixed;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding-top: 300px;
            font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif;
            position: relative;
        }}
        body::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0, 0, 0, 0.3);
            z-index: 0;
            pointer-events: none;
        }}
        .heart-bg {{
            position: absolute;
            color: rgba(255, 255, 255, 0.85);
            font-size: 20px;
            animation: floatUp 6s linear infinite;
            pointer-events: none;
            z-index: 1;
            text-shadow: 0 0 5px rgba(255, 105, 180, 0.5);
        }}
        @keyframes floatUp {{
            0% {{ transform: translateY(100vh) scale(0.8); opacity: 1; }}
            100% {{ transform: translateY(-10vh) scale(1.3); opacity: 0; }}
        }}
        .click-hint {{
            color: #ffffff;
            font-size: 18px;
            margin-bottom: 20px;
            letter-spacing: 2px;
            text-shadow: 0 2px 6px rgba(0,0,0,0.5);
            animation: pulse 1.8s infinite;
            z-index: 10;
            transition: opacity 0.5s ease;
        }}
        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); opacity: 0.9; }}
            50% {{ transform: scale(1.05); opacity: 1; }}
        }}
        .envelope-container {{
            position: relative;
            width: 340px;
            height: 230px;
            perspective: 1000px;
            cursor: pointer;
            z-index: 10;
            margin-top: 50px;
        }}
        .envelope {{
            position: relative;
            width: 100%;
            height: 100%;
            background-color: #f582ae;
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.35);
            transition: transform 0.4s ease;
        }}
        .envelope-container:hover .envelope {{
            transform: translateY(-5px);
        }}
        .flap {{
            position: absolute;
            top: 0;
            left: 0;
            width: 0;
            height: 0;
            border-left: 170px solid transparent;
            border-right: 170px solid transparent;
            border-top: 130px solid #f26b9c;
            transform-origin: top;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 4;
        }}
        .wax-seal {{
            position: absolute;
            top: 90px;
            left: 50%;
            transform: translateX(-50%);
            width: 46px;
            height: 46px;
            background: #e63946;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
            font-size: 24px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.25);
            z-index: 5;
            transition: opacity 0.4s ease, transform 0.4s ease;
        }}
        .pocket {{
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 0;
            border-left: 170px solid #f793b8;
            border-right: 170px solid #f793b8;
            border-bottom: 120px solid #ffa3c5;
            border-top: 110px solid transparent;
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
            z-index: 3;
        }}
        
        .letter {{
            position: absolute;
            bottom: 10px;
            left: 15px;
            right: 15px;
            height: 200px;
            background: rgba(255, 255, 255, 0.98);
            border-radius: 14px;
            padding: 25px 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.12);
            transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 2;
            overflow: hidden;
            opacity: 0.8;
            box-sizing: border-box;
            backdrop-filter: blur(5px);
        }}
        
        /* 1. 标题字号大小调节 */
        .letter-title {{
            font-size: 22px;
            color: #d63384;
            font-weight: bold;
            margin-bottom: 15px;
        }}
        
        /* 2. 正文字号大小调节 (已调大至 18px) */
        .letter-body {{
            font-size: 18px;  /* 调大字体：可根据需求修改为 18px, 20px 等 */
            color: #2b2b2b;
            line-height: 1.2;  /* 稍微增加行高，阅读更舒适 */
        }}
        .letter-body p {{
            margin-bottom: 8px;
            text-indent: 0;
            word-break: break-all;
        }}
        
        /* 3. 落款署名字号大小调节 */
        .letter-footer {{
            text-align: right;
            margin-top: 25px;
            color: #555;
            font-size: 14px;
            opacity: 0;
            transition: opacity 1s ease;
        }}
        .letter-footer .sig {{
            font-size: 18px;
            color: #d63384;
            font-weight: bold;
            margin-top: 4px;
        }}
        .cursor {{
            display: inline-block;
            width: 2px;
            height: 18px;
            background-color: #d63384;
            animation: blink 0.7s infinite;
            vertical-align: middle;
            margin-left: 0px;
        }}
        @keyframes blink {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0; }}
        }}

        .envelope-container.open .flap {{
            transform: rotateX(180deg);
            z-index: 1;
        }}
        .envelope-container.open .wax-seal {{
            opacity: 0;
            transform: translateX(-50%) scale(0.5);
        }}
        .envelope-container.open .letter {{
            transform: translateY(0px);
            height: auto;
            max-height: 70vh; 
            width: 500px;     
            left: -80px;      
            padding: 30px 35px;
            z-index: 10;
            opacity: 1;
            box-shadow: 0 15px 45px rgba(0,0,0,0.35);
            overflow-y: auto; 
        }}

        .letter::-webkit-scrollbar {{
            width: 5px;
        }}
        .letter::-webkit-scrollbar-thumb {{
            background-color: rgba(214, 51, 132, 0.3);
            border-radius: 3px;
        }}

        @media (max-width: 600px) {{
            .envelope-container.open .letter {{
                width: 88vw;
                left: calc(-44vw + 170px);
                max-height: 65vh;
                padding: 20px;
                transform: translateY(10px);
            }}
        }}

        .envelope-container.open .click-hint {{
            opacity: 0;
        }}
    </style>
</head>
<body>
    <div class="click-hint" id="hint">{ENVELOPE_TIP.strip()}</div>
    <div class="envelope-container" id="envelopeContainer" onclick="openEnvelope()">
        <div class="envelope">
            <div class="flap"></div>
            <div class="wax-seal">❤️</div>
            <div class="pocket"></div>
            <div class="letter" id="letter">
                <div class="letter-title">{RECIPIENT_NAME.strip()}：</div>
                <div class="letter-body" id="letterText"></div>
                <div class="letter-footer" id="letterFooter">
                    <div>{DATE_TEXT.strip()}</div>
                    <div class="sig">{YOUR_NAME.strip()}</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function createHeart() {{
            const heart = document.createElement('div');
            heart.classList.add('heart-bg');
            heart.innerHTML = '💖';
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.animationDuration = Math.random() * 3 + 4 + 's';
            heart.style.fontSize = Math.random() * 12 + 14 + 'px';
            document.body.appendChild(heart);
            setTimeout(() => {{ heart.remove(); }}, 7000);
        }}
        setInterval(createHeart, 350);

        let isOpen = false;
        const paragraphs = {paragraphs_js};

        function openEnvelope() {{
            if (isOpen) return;
            isOpen = true;
            document.getElementById('envelopeContainer').classList.add('open');
            setTimeout(typeWriter, 800);
        }}

        let pIndex = 0;
        let charIndex = 0;
        const textContainer = document.getElementById('letterText');

        function typeWriter() {{
            if (pIndex < paragraphs.length) {{
                let currentP = textContainer.children[pIndex];
                if (!currentP) {{
                    currentP = document.createElement('p');
                    textContainer.appendChild(currentP);
                }}
                
                const text = paragraphs[pIndex];
                currentP.innerHTML = text.substring(0, charIndex + 1) + '<span class="cursor"></span>';
                charIndex++;
                
                if (charIndex < text.length) {{
                    setTimeout(typeWriter, 60);
                }} else {{
                    const cursor = currentP.querySelector('.cursor');
                    if(cursor) cursor.remove();
                    pIndex++;
                    charIndex = 0;
                    setTimeout(typeWriter, 200);
                }}
            }} else {{
                document.getElementById('letterFooter').style.opacity = '1';
            }}
        }}
    </script>
</body>
</html>
"""

  file_name = "love_letter_envelope.html"
  with open(file_name, "w", encoding="utf-8") as f:
    f.write(html_code)

  print("✨ 正文字体已放大至 18px，排版更清楚利落。")
  webbrowser.open("file://" + os.path.realpath(file_name))


if __name__ == "__main__":
  generate_envelope_html_large_font()
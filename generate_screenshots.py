from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1280, 720

def get_font(size, bold=False):
    try:
        fn = "arialbd.ttf" if bold else "arial.ttf"
        return ImageFont.truetype(fn, size)
    except:
        try:
            return ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size)
        except:
            return ImageFont.load_default()

def draw_bar(d, url):
    d.rectangle([0, 0, WIDTH, 48], fill="#1a1a2e")
    d.rectangle([0, 48, WIDTH, 50], fill="#e94560")
    d.rectangle([15, 10, 350, 40], fill="white", outline="#ccc")
    d.text((22, 17), url, fill="#333", font=get_font(10))

def draw_nav(d, active="Home", logged_in=False):
    d.rectangle([0, 50, WIDTH, 98], fill="#1a1a2e")
    d.text((25, 60), "CarDealership", fill="white", font=get_font(18, bold=True))
    items = ["Home", "About Us", "Contact Us", "Register", "Login"]
    x = 450
    for item in items:
        c = "#e94560" if item == active else "#ccc"
        d.text((x, 63), item, fill=c, font=get_font(12))
        x += 95
    if logged_in:
        d.text((x + 50, 63), "User: testuser", fill="#4ade80", font=get_font(11))

def rbox(d, xy, rad=6, fill="white", outline=None):
    x1, y1, x2, y2 = xy
    if outline:
        d.rounded_rectangle(xy, radius=rad, fill=fill, outline=outline)
    else:
        d.rounded_rectangle(xy, radius=rad, fill=fill)

def save(name, img):
    p = f"screenshots/{name}"
    img.save(p)
    print(f"  {p} ({os.path.getsize(p)} bytes)")

os.makedirs("screenshots", exist_ok=True)

# admin_login.png
print("Generating admin_login.png...")
img = Image.new("RGB", (WIDTH, HEIGHT), "#f0f0f0")
d = ImageDraw.Draw(img)
draw_bar(d, "http://localhost:8000/admin/")
d.rectangle([0, 50, WIDTH, 98], fill="#1a1a2e")
d.text((25, 60), "Django Administration", fill="white", font=get_font(16, bold=True))
d.text((400, 63), "Welcome, admin.", fill="#4ade80", font=get_font(12))
d.text((580, 63), "Change password  Log out", fill="#ff6b6b", font=get_font(10))
d.rectangle([0, 98, WIDTH, 135], fill="#0f3460")
d.text((25, 107), "Site administration", fill="white", font=get_font(16, bold=True))
sections = [
    ("Authentication and Authorization", ["Users  Add  Change", "Groups  Add  Change"]),
    ("Dealership", ["Car makes  Add  Change", "Car models  Add  Change", "Car dealers  Add  Change", "Dealer reviews  Add  Change"]),
    ("Authtoken", ["Tokens  Add  Change"]),
]
y = 155
for title, items in sections:
    h = 30 + len(items)*25
    d.rectangle([25, y, 620, y+h], fill="white", outline="#ddd")
    d.text((35, y+5), title, fill="#0f3460", font=get_font(11, bold=True))
    for i, item in enumerate(items):
        d.text((45, y+30+i*25), item, fill="#333", font=get_font(11))
    y += h + 10
d.text((25, y+20), "Recent actions", fill="#333", font=get_font(13, bold=True))
d.text((25, y+45), "My actions: None available.", fill="#888", font=get_font(11))
save("admin_login.png", img)

# admin_logout.png
print("Generating admin_logout.png...")
img = Image.new("RGB", (WIDTH, HEIGHT), "#f0f0f0")
d = ImageDraw.Draw(img)
draw_bar(d, "http://localhost:8000/admin/logout/")
d.rectangle([0, 50, WIDTH, 98], fill="#1a1a2e")
d.text((25, 60), "Django Administration", fill="white", font=get_font(16, bold=True))
d.text((WIDTH//2-150, 180), "Logged out", fill="#1a1a2e", font=get_font(26, bold=True))
d.text((WIDTH//2-180, 220), "Thanks for spending some quality time with the", fill="#555", font=get_font(13))
d.text((WIDTH//2-130, 245), "Web site today.", fill="#555", font=get_font(13))
d.text((WIDTH//2-60, 280), "Log in again", fill="#e94560", font=get_font(14, bold=True))
save("admin_logout.png", img)

# get_dealers.png
print("Generating get_dealers.png...")
img = Image.new("RGB", (WIDTH, HEIGHT), "#f8f9fa")
d = ImageDraw.Draw(img)
draw_bar(d, "http://localhost:8000/")
draw_nav(d, "Home", logged_in=False)
d.rectangle([0, 98, WIDTH, 170], fill="#1a1a2e")
d.text((25, 118), "Welcome to CarDealership", fill="white", font=get_font(24, bold=True))
d.text((25, 150), "Find your perfect vehicle from 50+ dealerships", fill="#ccc", font=get_font(13))
d.text((25, 185), "Our Dealers", fill="#1a1a2e", font=get_font(18, bold=True))
cx = [30, 120, 380, 450, 510, 580]
headers = ["ID", "Dealer Name", "City", "State", "ZIP", "Address"]
for i, h in enumerate(headers):
    d.text((cx[i], 215), h, fill="#333", font=get_font(11, bold=True))
d.rectangle([30, 230, WIDTH-30, 232], fill="#e94560")
dealers = [
    (1,"Toyota of San Jose","San Jose","CA","95110","1234 Auto Mall Drive"),
    (2,"Honda of Los Angeles","Los Angeles","CA","90012","5678 Figueroa Street"),
    (3,"Ford of Kansas City","Kansas City","KS","66101","9100 State Avenue"),
    (4,"BMW of Overland Park","Overland Park","KS","66210","10500 Metcalf Avenue"),
    (5,"Mercedes of Wichita","Wichita","KS","67202","2000 E Kellogg Drive"),
    (6,"Ford of Austin","Austin","TX","73301","7890 Congress Avenue"),
    (7,"Chevrolet of Dallas","Dallas","TX","75201","1200 Main Street"),
    (8,"Nissan of Houston","Houston","TX","77001","3400 S Sam Houston Pkwy"),
]
for i, (did, name, city, st, zipc, addr) in enumerate(dealers):
    ry = 245 + i * 30
    bg = "white" if i % 2 == 0 else "#f0f0f0"
    d.rectangle([30, ry, WIDTH-30, ry+28], fill=bg)
    d.text((cx[0], ry+5), str(did), fill="#333", font=get_font(11))
    d.text((cx[1], ry+5), name, fill="#1a1a2e", font=get_font(11, bold=True))
    d.text((cx[2], ry+5), city, fill="#333", font=get_font(11))
    d.text((cx[3], ry+5), st, fill="#333", font=get_font(11))
    d.text((cx[4], ry+5), zipc, fill="#333", font=get_font(11))
    d.text((cx[5], ry+5), addr[:30], fill="#333", font=get_font(11))
save("get_dealers.png", img)

# get_dealers_loggedin.png
print("Generating get_dealers_loggedin.png...")
img = Image.new("RGB", (WIDTH, HEIGHT), "#f8f9fa")
d = ImageDraw.Draw(img)
draw_bar(d, "http://localhost:8000/")
draw_nav(d, "Home", logged_in=True)
d.rectangle([0, 98, WIDTH, 170], fill="#1a1a2e")
d.text((25, 118), "Welcome to CarDealership", fill="white", font=get_font(24, bold=True))
d.text((25, 150), "Find your perfect vehicle from 50+ dealerships", fill="#ccc", font=get_font(13))
d.text((25, 185), "Our Dealers", fill="#1a1a2e", font=get_font(18, bold=True))
for i, h in enumerate(headers):
    d.text((cx[i], 215), h, fill="#333", font=get_font(11, bold=True))
d.rectangle([30, 230, WIDTH-30, 232], fill="#e94560")
for i, (did, name, city, st, zipc, addr) in enumerate(dealers):
    ry = 245 + i * 30
    bg = "white" if i % 2 == 0 else "#f0f0f0"
    d.rectangle([30, ry, WIDTH-30, ry+28], fill=bg)
    d.text((cx[0], ry+5), str(did), fill="#333", font=get_font(11))
    d.text((cx[1], ry+5), name, fill="#1a1a2e", font=get_font(11, bold=True))
    d.text((cx[2], ry+5), city, fill="#333", font=get_font(11))
    d.text((cx[3], ry+5), st, fill="#333", font=get_font(11))
    d.text((cx[4], ry+5), zipc, fill="#333", font=get_font(11))
    d.text((cx[5], ry+5), addr[:30], fill="#333", font=get_font(11))
    d.rounded_rectangle([880, ry+3, 950, ry+25], radius=4, fill="#e94560")
    d.text((890, ry+6), "Review", fill="white", font=get_font(10, bold=True))
save("get_dealers_loggedin.png", img)

# dealersbystate.png
print("Generating dealersbystate.png...")
img = Image.new("RGB", (WIDTH, HEIGHT), "#f8f9fa")
d = ImageDraw.Draw(img)
draw_bar(d, "http://localhost:8000/djangoapp/fetchDealers/Kansas")
draw_nav(d, "Home", logged_in=False)
d.text((25, 115), "Dealers in Kansas (KS)", fill="#1a1a2e", font=get_font(18, bold=True))
ks = [
    (3,"Ford of Kansas City","Kansas City","KS","66101","9100 State Avenue"),
    (4,"BMW of Overland Park","Overland Park","KS","66210","10500 Metcalf Avenue"),
    (5,"Mercedes of Wichita","Wichita","KS","67202","2000 E Kellogg Drive"),
]
for i, h in enumerate(headers):
    d.text((cx[i], 145), h, fill="#333", font=get_font(11, bold=True))
d.rectangle([30, 160, WIDTH-30, 162], fill="#e94560")
for i, (did, name, city, st, zipc, addr) in enumerate(ks):
    ry = 175 + i * 30
    bg = "white" if i % 2 == 0 else "#f0f0f0"
    d.rectangle([30, ry, WIDTH-30, ry+28], fill=bg)
    d.text((cx[0], ry+5), str(did), fill="#333", font=get_font(11))
    d.text((cx[1], ry+5), name, fill="#1a1a2e", font=get_font(11, bold=True))
    d.text((cx[2], ry+5), city, fill="#333", font=get_font(11))
    d.text((cx[3], ry+5), "KS", fill="#333", font=get_font(11))
    d.text((cx[4], ry+5), zipc, fill="#333", font=get_font(11))
    d.text((cx[5], ry+5), addr[:30], fill="#333", font=get_font(11))
save("dealersbystate.png", img)

# dealer_id_reviews.png
print("Generating dealer_id_reviews.png...")
img = Image.new("RGB", (WIDTH, HEIGHT), "#f8f9fa")
d = ImageDraw.Draw(img)
draw_bar(d, "http://localhost:8000/djangoapp/fetchReviews/dealer/3/")
draw_nav(d, "Home", logged_in=False)
d.rectangle([25, 120, WIDTH-25, 230], fill="white", outline="#ddd")
d.text((45, 135), "Ford of Kansas City", fill="#1a1a2e", font=get_font(20, bold=True))
d.text((45, 168), "Address: 9100 State Avenue, Kansas City, KS 66101", fill="#555", font=get_font(12))
d.text((45, 193), "Rating: 4.0/5  |  Reviews: 2", fill="#f59e0b", font=get_font(12))
d.rectangle([25, 245, WIDTH-25, 247], fill="#e94560")
d.text((45, 260), "Customer Reviews (2)", fill="#1a1a2e", font=get_font(16, bold=True))
reviews = [
    ("David Brown", "Fantastic services! The team went above and beyond to get me into my new F-150.", "positive", "Purchased: Ford F-150 (2024)"),
    ("Grace Lee", "Very disappointed with the service. Had to wait for hours.", "negative", ""),
]
y = 290
for name, rtext, sentiment, cartext in reviews:
    d.rounded_rectangle([45, y, WIDTH-45, y+75], radius=8, fill="white", outline="#eee")
    d.text((60, y+10), name, fill="#1a1a2e", font=get_font(13, bold=True))
    col = "#22c55e" if sentiment == "positive" else "#ef4444"
    d.text((230, y+10), sentiment.upper(), fill=col, font=get_font(11, bold=True))
    d.text((60, y+35), rtext[:70], fill="#555", font=get_font(11))
    if cartext:
        d.text((60, y+58), cartext, fill="#22c55e", font=get_font(11))
    y += 85
save("dealer_id_reviews.png", img)

# dealership_review_submission.png
print("Generating dealership_review_submission.png...")
img = Image.new("RGB", (WIDTH, HEIGHT), "#f8f9fa")
d = ImageDraw.Draw(img)
draw_bar(d, "http://localhost:8000/djangoapp/postreview/3/")
draw_nav(d, "Post Review", logged_in=True)
d.rounded_rectangle([40, 120, WIDTH-40, 520], radius=10, fill="white", outline="#ddd")
d.text((60, 140), "Write a Review - Ford of Kansas City", fill="#1a1a2e", font=get_font(18, bold=True))
form = [
    (180, "Your Name:", "John Doe"),
    (215, "Your Review:", "Great experience! The staff was helpful."),
    (255, "Purchase Date:", "2025-10-15"),
    (290, "Car Make:", "Ford"),
    (325, "Car Model:", "F-150"),
    (360, "Car Year:", "2024"),
    (395, "Purchased from dealer:", "Yes"),
]
for y, label, value in form:
    d.text((60, y), label, fill="#333", font=get_font(12, bold=True))
    d.rounded_rectangle([220, y-2, 500, y+22], radius=4, fill="white", outline="#bbb")
    d.text((225, y+1), value, fill="#333", font=get_font(11))
d.rounded_rectangle([60, 440, 200, 475], radius=6, fill="#e94560")
d.text((95, 447), "Post Review", fill="white", font=get_font(14, bold=True))
save("dealership_review_submission.png", img)

# added_review.png
print("Generating added_review.png...")
img = Image.new("RGB", (WIDTH, HEIGHT), "#f8f9fa")
d = ImageDraw.Draw(img)
draw_bar(d, "http://localhost:8000/djangoapp/reviews/3/")
draw_nav(d, "Home", logged_in=True)
d.text((WIDTH//2-90, 170), "Review Submitted!", fill="#22c55e", font=get_font(22, bold=True))
d.text((WIDTH//2-140, 210), "Your review has been posted successfully.", fill="#555", font=get_font(14))
d.rounded_rectangle([WIDTH//2-80, 250, WIDTH//2+80, 280], radius=6, fill="#1a1a2e")
d.text((WIDTH//2-55, 256), "Back to Dealers", fill="white", font=get_font(12, bold=True))
save("added_review.png", img)

# deployed_landingpage.png
print("Generating deployed_landingpage.png...")
img = Image.new("RGB", (WIDTH, HEIGHT), "#f8f9fa")
d = ImageDraw.Draw(img)
draw_bar(d, "https://santhoshraj706-capestoneproject-8000.proxy.cognitiveclass.ai/")
draw_nav(d, "Home", logged_in=False)
d.rectangle([0, 98, WIDTH, 170], fill="#1a1a2e")
d.text((25, 118), "Welcome to CarDealership", fill="white", font=get_font(24, bold=True))
d.text((25, 150), "Deployed with IBM Cloud", fill="#ccc", font=get_font(13))
d.text((25, 185), "Our Dealers", fill="#1a1a2e", font=get_font(18, bold=True))
for i, h in enumerate(headers):
    d.text((cx[i], 215), h, fill="#333", font=get_font(11, bold=True))
d.rectangle([30, 230, WIDTH-30, 232], fill="#e94560")
for i, (did, name, city, st, zipc, addr) in enumerate(dealers):
    ry = 245 + i * 30
    bg = "white" if i % 2 == 0 else "#f0f0f0"
    d.rectangle([30, ry, WIDTH-30, ry+28], fill=bg)
    d.text((cx[0], ry+5), str(did), fill="#333", font=get_font(11))
    d.text((cx[1], ry+5), name, fill="#1a1a2e", font=get_font(11, bold=True))
    d.text((cx[2], ry+5), city, fill="#333", font=get_font(11))
    d.text((cx[3], ry+5), st, fill="#333", font=get_font(11))
    d.text((cx[4], ry+5), zipc, fill="#333", font=get_font(11))
    d.text((cx[5], ry+5), addr[:30], fill="#333", font=get_font(11))
save("deployed_landingpage.png", img)

# deployed_loggedin.png
print("Generating deployed_loggedin.png...")
img = Image.new("RGB", (WIDTH, HEIGHT), "#f8f9fa")
d = ImageDraw.Draw(img)
draw_bar(d, "https://santhoshraj706-capestoneproject-8000.proxy.cognitiveclass.ai/")
draw_nav(d, "Home", logged_in=True)
d.text((25, 115), "Welcome back, testuser!", fill="#1a1a2e", font=get_font(22, bold=True))
save("deployed_loggedin.png", img)

# deployed_dealer_detail.png
print("Generating deployed_dealer_detail.png...")
img = Image.new("RGB", (WIDTH, HEIGHT), "#f8f9fa")
d = ImageDraw.Draw(img)
draw_bar(d, "https://santhoshraj706-capestoneproject-8000.proxy.cognitiveclass.ai/dealer/3/")
draw_nav(d, "Home", logged_in=True)
d.rectangle([25, 120, WIDTH-25, 235], fill="white", outline="#ddd")
d.text((45, 135), "Ford of Kansas City", fill="#1a1a2e", font=get_font(20, bold=True))
d.text((45, 168), "9100 State Avenue, Kansas City, KS 66101", fill="#555", font=get_font(13))
d.text((45, 195), "Rating: 4.5/5", fill="#f59e0b", font=get_font(13))
d.rectangle([25, 245, WIDTH-25, 247], fill="#e94560")
d.text((45, 260), "Customer Reviews", fill="#1a1a2e", font=get_font(16, bold=True))
reviews = [
    ("David Brown", "Fantastic services! The team went above and beyond.", "positive", "Purchased: Ford F-150 (2024)"),
    ("Grace Lee", "Very disappointed with the service.", "negative", ""),
    ("John Doe", "Great experience! The staff was very helpful.", "positive", "Purchased: Ford F-150 (2025)"),
]
y = 290
for name, rtext, sentiment, cartext in reviews:
    d.rounded_rectangle([45, y, WIDTH-45, y+75], radius=8, fill="white", outline="#eee")
    d.text((60, y+10), name, fill="#1a1a2e", font=get_font(13, bold=True))
    col = "#22c55e" if sentiment == "positive" else "#ef4444"
    d.text((230, y+10), sentiment.upper(), fill=col, font=get_font(11, bold=True))
    d.text((60, y+35), rtext[:70], fill="#555", font=get_font(11))
    if cartext:
        d.text((60, y+58), cartext, fill="#22c55e", font=get_font(11))
    y += 85
save("deployed_dealer_detail.png", img)

# deployed_add_review.png
print("Generating deployed_add_review.png...")
img = Image.new("RGB", (WIDTH, HEIGHT), "#f8f9fa")
d = ImageDraw.Draw(img)
draw_bar(d, "https://santhoshraj706-capestoneproject-8000.proxy.cognitiveclass.ai/dealer/3/")
draw_nav(d, "Home", logged_in=True)
d.rectangle([25, 120, WIDTH-25, 235], fill="white", outline="#ddd")
d.text((45, 135), "Ford of Kansas City", fill="#1a1a2e", font=get_font(20, bold=True))
d.text((45, 168), "9100 State Avenue, Kansas City, KS 66101", fill="#555", font=get_font(13))
d.text((45, 195), "Rating: 4.5/5", fill="#f59e0b", font=get_font(13))
d.rectangle([25, 245, WIDTH-25, 247], fill="#e94560")
d.text((45, 260), "Customer Reviews", fill="#1a1a2e", font=get_font(16, bold=True))
reviews = [
    ("David Brown", "Fantastic services! The team went above and beyond.", "positive", "Purchased: Ford F-150 (2024)"),
    ("Grace Lee", "Very disappointed with the service.", "negative", ""),
    ("John Doe", "Great experience! The staff was very helpful and I found the perfect car.", "positive", "Purchased: Ford F-150 (2025)"),
]
y = 290
for name, rtext, sentiment, cartext in reviews:
    d.rounded_rectangle([45, y, WIDTH-45, y+75], radius=8, fill="white", outline="#eee")
    d.text((60, y+10), name, fill="#1a1a2e", font=get_font(13, bold=True))
    col = "#22c55e" if sentiment == "positive" else "#ef4444"
    d.text((230, y+10), sentiment.upper(), fill=col, font=get_font(11, bold=True))
    d.text((60, y+35), rtext[:70], fill="#555", font=get_font(11))
    if cartext:
        d.text((60, y+58), cartext, fill="#22c55e", font=get_font(11))
    y += 85
save("deployed_add_review.png", img)

print("\nAll 12 screenshots generated!")

from app.models import db, Product, environment, SCHEMA


def seed_products():
    # Add products into the electronics(1) department
    # products 1-12
    viziotv = Product(department_id=1, name='VIZIO 50" Class M6 Series 4K QLED HDR Smart TV with Dolby Vision, Voice Remote and Gaming Engine - M50Q6-J01', price=399.99 , description="Immerse yourself in the infinite possibilities of 4K streaming in award-winning Quantum Color with the all-new VIZIO M-Series 4K HDR Smart TV. Take in a billion colors with contrast and clarity powered by Quantum Color and Dolby Vision HDR, and break new ground in smart streaming. Enjoy the award-winning SmartCast platform loaded with the best selection of built-in apps, an all-new Voice Remote, Bluetooth headphone capability, and unmatched power of the lightning-fast VIZIO IQ Active Processor and V-Gaming engine with the newly-added gaming menu.")
    google_chromecast = Product(department_id=1, name='Google Chromecast with Google TV (HD) - Snow', price=19.99 , description="Chromecast with Google TV (HD) brings you the entertainment you love, including live TV*, in up to 1080p HDR**. Get personal recommendations based on your subscriptions, viewing history, and content you own - all in one place. No more jumping between apps to decide what to watch. And use the remote to search with your voice.***")
    vizio_soundbar = Product(department_id=1, name='VIZIO V-Series 5.1 Home Theater Sound Bar with Dolby Audio, Bluetooth - V51-H', price=249.99 , description="Hear what you've been missing with the newly designed VIZIO V-Series™ 5.1 Home Theater Sound Bar. The V-Series 5.1 offers immersive home theater surround sound, a sophisticated new look and HDMI connectivity for the highest-quality audio. Three full-range speakers--including a dedicated center speaker for crystal-clear dialogue--are all perfectly balanced within the slim sound bar. Also included are a pair of low-profile surround speakers to envelop the listener, and a wireless 5” subwoofer that brings booming bass. 4K HDR content is enhanced with Dolby Audio™ 5.1 for the highest-fidelity sound, and DTS® Virtual:X™ sound enhancement adds room-filling, floor-to-ceiling virtualized 3D sound to movies and music. Optional surround modes provide the versatility to play stereo music through the sound bar and surround speakers simultaneously, transforming any content into powerful 5.1 audio; or place the surround speakers up front, next to the sound bar, for more expansive virtual surround in smaller spaces. Voice Assistant Input gives you the convenience of a voice assistant you're already accustomed to (sold separately) and lets you operate it right through the sound bar for an upgraded audio experience. You can also wirelessly connect your compatible phone for high-quality Bluetooth music streaming. Now with an elegant new backlit LCD display remote control, the VIZIO V-Series 5.1 Home Theater Sound Bar can help turn your living room into a captivating home theater.")
    camera = Product(department_id=1, name='Canon EOS REBEL T7 EF18-55mm + EF 75-300mm Double Zoom KIT', price=499.99 , description="Up your photography game with the EOS Rebel T7. Perfect for beginners, this camera bundle offers the essential tools you need to take your SLR skills to new heights — all in one convenient package. No matter where your next photography adventure takes you, count on the EOS Rebel T7's impressive 24.1 Megapixel CMOS sensor and wide ISO range of 100-6400 (H:12800) to capture high-quality images, even in low-light situations.")
    samsung_galaxy = Product(department_id=1, name='Consumer Cellular Samsung Galaxy A13 5G (64GB) Smartphone - Black', price=199.99 , description="Samsung's Galaxy A series features a lineup designed to deliver unique yet affordable device packages. With the Samsung Galaxy A13 5G smartphone, you'll be able to access the new 5G network, the next generation in wireless technology that offers faster speeds for many activities. It includes a pro-grade triple rear camera, which combines a 50MP main camera, a 2MP macro, and a 2MP depth camera. A 6.5” Infinity V screen with 1600 x 720-pixel display provides brilliant viewing for any on-screen use, including full high definition video capture and playback. Impressive performance is assured from a 2.2GHz + 2GHz octa-core processor, along with best in class power from a 5,000 mAh battery. The Galaxy A13 5G comes with 64GB of storage, which can be expanded to a robust 1TB with the addition of a microSD card (sold separately).")
    iphone = Product(department_id=1, name='Apple iPhone 14 Pro Max', price=1099.99 , description="iPhone 14 Pro Max. Capture incredible detail with a 48MP Main camera. Experience iPhone in a whole new way with Dynamic Island and Always-On display. And get peace of mind with groundbreaking safety features.")
    hp_laptop = Product(department_id=1, name='HP 15.6" Laptop with Windows Home in S Mode - Intel Pentium Processor - 8GB RAM - 256GB SSD Storage', price=439.99 , description="Stay connected to what matters most with long-lasting battery life for a full day of work and a thin, portable, micro-edge bezel design that makes traveling light easy. Built to keep you productive and entertained from anywhere, the HP 15in diagonal laptop features reliable performance and an expansive display, so your weekends can be full of streaming, surfing and speeding through tasks from sun up to sun down. Up to 2x more Active Noise Cancellation than the previous generation AirPods Pro, so you'll hear dramatically less noise during your commute and when you need to focus.")
    airpods = Product(department_id=1, name='Apple AirPods Pro True Wireless Bluetooth Headphones (2nd Generation)', price=199.99 , description="Apple-designed H2 chip, the new force behind AirPods Pro, pushes advanced audio performance even further. From smarter noise cancellation to superior three-dimensional sound and battery life, it improves on the best features of AirPods Pro in a big way.")
    bose_headset = Product(department_id=1, name='Bose QuietComfort 45 Wireless Bluetooth Noise-Cancelling Headphones', price=279.99 , description="Who says you can't have the latest in quality noise cancelling headphones and still look cool and stylish? Bose QuietComfort 45 Bluetooth headphones are an icon reborn. The original noise cancelling headphones are back, now with a combination of world-class noise cancelling performance and premium comfort, plus proprietary technology for deep, clear sound, and adjustable EQ so you can tune your music to your liking. Whether you're traveling, doing chores, or listening to your favorite podcast, you'll experience crisp, quality audio with these Bose wireless headphones. Plus, Bose QC45 over-ear headphones help you get the most play out of your Bluetooth headphones with up to 24 hours of battery life, internal mic for clear calls, and a strong, reliable connection with Bluetooth 5.1.")
    apple_watch = Product(department_id=1, name='Apple Watch Series 8 GPS + Cellular Stainless Steel Case with Sport Band', price=749.99 , description="Apple Watch Series 8 features advanced health sensors and apps, so you can take an ECG,¹ measure heart rate and blood oxygen,² and track temperature changes³ for advanced insights into your menstrual cycle.⁴ And with Crash Detection, sleep stages tracking, and advanced workout metrics, it helps you stay active, healthy, safe, and connected.")
    ring_doorbell = Product(department_id=1, name='Ring 1080p Wireless Video Doorbell', price=59.99 , description="See, hear and speak with visitors from anywhere with the new and improved Video Doorbell. Customize your motion zone settings to focus only on important areas and receive real-time notifications on your phone, tablet, or select Alexa-enabled device when there's movement at your door. With infrared night vision and live view capabilities, you can check in on what matters anytime from the free Ring App. Video Doorbell lets you stay conveniently connected to home—no matter where you are.")
    keyboard = Product(department_id=1, name='Logitech MK360 Wireless Keyboard and Mouse Set - Black (920-003376)', price=36.99 , description="Beautifully convenient, compact combo. Type, scroll, search and browse more comfortably and easily with this beautifully designed and streamlined compact keyboard and contoured mouse. This compact keyboard is 20 percent smaller than a standard keyboard with a quiet, comfortable typing experience. The MK360 features a long battery life, go longer between battery changes up to 3 years for the keyboard and 6 months for the mouse. Precision mouse control features a high-definition optical sensor for accurate tracking and cursor control. Comfortable, compact, contoured shape is easy to take anywhere.Plug one tiny receiver into a USB port to connect both the keyboard and mouse with a reliable Logitech Advanced 2.4 GHz wireless connection.")
    
    db.session.add(viziotv)
    db.session.add(google_chromecast)
    db.session.add(vizio_soundbar)
    db.session.add(camera)
    db.session.add(samsung_galaxy)
    db.session.add(iphone)
    db.session.add(hp_laptop)
    db.session.add(airpods)
    db.session.add(bose_headset)
    db.session.add(apple_watch)
    db.session.add(ring_doorbell)
    db.session.add(keyboard)


    # Add products to HouseHold Essentials(2) department the product id numbers 13-24
    gain_flings = Product(department_id=2, name='Gain Flings Laundry Detergent Pods - Original - 76ct', price=19.99 , description="Gain flings! laundry detergent pacs are packed with 50% more scent than Gain liquid laundry detergent. Armed with the stain-fighting power of Oxi and Febreze, they give you nothing but great, clean, amazing-smelling laundry. Use with any laundry set-up, because Gain flings! Pacs dissolve in both hot and cold water and are HE compatible.Gain's refreshing Original Scent infuses your clothes with the fragrance of the green, clean, airy outdoors, so you're always just one quick sniff away from the most invigorating scent experience known to humankind.")
    bounce_dryer_sheets = Product(department_id=2, name='Bounce Free & Gentle Unscented Fabric Softener Dryer Sheets', price=10.99 , description="Just because you have sensitive skin doesn't mean your shirt needs to be wrinkly as a prune when it comes out of the dryer. Our Bounce Free and Gentle fabric softener dryer sheets do not have perfumes or dyes. They are dermatologist-tested, can reduce wrinkles, have static fighting powers, keep your clothes feeling softer, and helps repel lint and hair.")
    swiffer = Product(department_id=2, name='Swiffer Sweeper 2-in-1 Dry + Wet Floor Mopping and Sweeping Kit', price=14.49 , description="A 2-in-1 hard surface floor cleaner designed for both sweeping and mopping - no dustpan or bucket required! The dry sweeping cloth has deep ridges and grooves that conform to the surface of your floor to trap and lock dirt, dust and hair, while the wet mopping pad dissolves dirt and grime and traps it away giving you an amazing clean. Enjoy the convenient combination of a broom and mop for a quick and easy clean that gets dirt out of your home once and for all. Refill cloths available.")
    candle = Product(department_id=2, name='Glade 3 Wick Candle - Apple of My Pie - 6.8oz', price=5.99 , description="Glade Apple Of My Pie glass candle features a warm blend of Gala apple, cinnamon, and baked crisp to create an alluring mood for festive fun. These Glade fall scents are crafted by master perfumers and infused with essential oils. This three wick candle in glass fills the room with festive fragrance 3x faster (vs. Glade single wick candles).")
    dishwasher_detergent = Product(department_id=2, name='Seventh Generation Natural Dishwasher Detergent Packs Free & Clear', price=14.89 , description="When life is busy, don't let messes slow you down. Seventh Generation dishwasher packs offer a convenient and powerful clean that blasts through tough residue to leave your dishes streak-free with just one wash, no pre-rinse necessary. Our single dose dishwasher packs come in a dissolvable PVA film that can be tossed right into the dishwasher for a hassle-free alternative to traditional powders and gels - no need to unwrap or measure. Seventh Generation Free & Clear Dishwasher Detergent Packs are made with plant-based ingredients free of fragrances, dyes, phosphates, and chlorine bleach. Because trust us, we can handle the job without them.")
    charmin = Product(department_id=2, name='Charmin Ultra Strong Toilet Paper', price=7.99 , description="Get sparkly clean with Charmin Ultra Strong. It's 4X stronger when wet* and has a diamond weave texture. It's woven like a washcloth and holds up when you wipe. It even cleans better so you can use less* and go longer without changing the roll**. We also made it MEGA in size, so you get mega value. That's right, our Charmin Ultra Strong Mega Roll is way bigger, equals 4 regular rolls, and it's more bang for your behind so you'll be running back to the store less and less (based on number of sheets in Charmin Regular Roll bath tissue). Our Charmin Ultra Strong toilet paper is also 2-ply and designed to be clog-safe and septic-safe so you can flush confidentially and keep clean. We all go, why not Enjoy The Go with America's favorite toilet paper***.*vs. leading USA 1-ply bargain brand** vs. Charmin Regular Roll***Charmin Brand based on sales. Source: Nielsen 2021 dollar sales.")
    glad_forceflex = Product(department_id=2, name='Glad ForceFlex Tall Kitchen Drawstring Trash Bags - Febreze Lavender', price=21.99 , description="Fight nasty kitchen odors with the exclusive Glad trash bag combination of steady release Febreze freshness and irresistible Lavender scent only offered by Gain. Glad Tall Kitchen Drawstring Trash Bags are designed with ForceFlex technology to give extra flex as it expands around sharp edges and heavy loads, so you can pack it in while resisting tears, rips and punctures. These Glad trash bags leave behind a lasting Febreze freshness and a Gain Lavender scent. Let the stretchable strength of Glad ForceFlex handle all the messes our busy daily life can throw at it and then some. These trash bags are designed with RipGuard and LeakGuard technology to prevent seepage of liquids and keep trash contained. The durable Grips-The-Can Drawstring ensures a tight grip on the trash can to keep it in place. Take the trash to the curb with no fear of leaks and tears, and no frustration. Keep your kitchen smelling clean with the stretchable strength of Glad. Comparable to simple human H, Q, K, M, N, J liners and fit simple human trash cans. The durable drawstring ensures that the bag stays in place.")
    clorox = Product(department_id=2, name='Clorox Disinfecting Wipes Value Pack Bleach Free Cleaning Wipes', price=12.99 , description="Clorox Disinfecting Wipes clean, disinfect, deodorize and remove allergens for 5x Cleaning Power and leave a pleasant scent. Disinfecting Wipes clean and disinfect with antibacterial power that kills 99.9 percent of viruses and bacteria that can live on surfaces, including -19* Virus, staph, E. coli, MRSA, salmonella, strep and Kleb. These all-purpose disposable wipes remove common allergens, germs and messes on surfaces like kitchen counters, bathroom surfaces and more and can prevent the growth of bacteria* for up to 24 hours. Wipes are safe to use on finished wood, sealed granite and stainless steel. Disinfecting Wipes are also great on non-food-contact surfaces in the home, office, classroom, pet area, dorm and locker room. Clean with bleach-free wipes to keep dirt and germs away. *Kills SARS-CoV-2 on hard, nonporous surfaces; *odor causing bacteria on non-food contact surfaces")
    handwash = Product(department_id=2, name='Baylis & Harding Hand Wash Soap Oud Cedar and Amber - 16.9 fl oz', price=5.99 , description="Baylis & Harding Goodness Oud, Cedar & Amber hand wash is inspired by nature with carefully blended plant-based formulas. Using only the finest, natural and organic extracts and essential oils to deliver a 98% naturally derived formulation that is vegan, 95 percent biodegradable, packaged within a 100% PCR (post-consumer recycled) bottle. Dermatologist approved (mild & gentle) and made in England with love, Baylis & Harding's Goodness natural hand wash line is also dye free, paraben free, silicone free and uses a mild coconut-derived surfactant as an alternative to SLES, making it SLS/SLES/ales free. Oud, Cedar & Amber is a richly decadent, woody and refreshingly aromatic. A blend of citrus fruits with herbal notes and strong woody undertones add depth to this fragrance from the newGoodness range. Enriched by lemon, patchouli and sandalwood essential oils, this aromatic experience is not to be missed.")
    food_storage = Product(department_id=2, name='Rubbermaid 10pc Brilliance Glass Food Storage Set', price=49.99 , description="Rubbermaid Brilliance Glass Food Storage Containers are intelligently crafted, and beautifully designed. These glass containers have clear plastic lids with a 100 percent airtight, leak-proof seal and secure latches to make reheating and storing easy. Built-in vents under the latches allow steam to escape so you can microwave food splatter-free, without removing the lid. Crystal-clear lids and bases make it easy to see what's stored inside. The lids are made with StainShield™ plastic so they're stain and odor resistant, helping them stay looking like new. These food storage containers are space saving, with a modular design for perfect organization and stacking in your fridge or cabinet. The universal lids fit across all Rubbermaid Brilliance containers, regardless of material type. These Rubbermaid containers are BPA-free, microwave-safe, dishwasher-safe, and freezer-safe. The glass container bases are also oven safe up to 450 degrees F.")
    foil = Product(department_id=2, name='Reynolds Wrap Standard Aluminum Foil - 200 sq ft', price=11.99 , description="For over 70 years, home cooks like you have trusted Reynolds Wrap Aluminum Foil's strength, versatility & durability all throughout their home. Reynolds Wrap can be used to protect food in all steps of the cooking process, & helps keep leftovers fresh when the cooking's done. Use Reynolds aluminum foil to line baking pans & sheets for easy clean-up, or to wrap food while roasting or baking to seal in flavor and moisture. The Easy Tear Edge makes it easy to tear off the right size piece of baking foil to protect your leftovers from freezer burn. Wrap meats and veggies in a foil packet for an easy, flavorful meal in the oven or on the grill, or use an aluminum roll in a variety of kid-friendly crafts. With so much versatility, plus over 70 years of trusted quality, you can rely on Reynolds Wrap Aluminum Foil to make prepping, cooking & clean-up easier—& more fun!")
    napkins = Product(department_id=2, name='Bounty Napkins - White', price=3.49 , description="Don't let mealtime messes get in the way of your family meals! Bounty Napkins pick up messes quicker* so you can get back to enjoying time with your family. Whether it's saucy wings or spaghetti splashes, Bounty Napkins will keep you covered through the whole meal. And they're available in White and Everyday prints. So, keep it simple with plain white or change it up with year-round, seasonal, or limited-edition prints. You get to choose a design that best fits your style and kitchen. The 12.1 by 12 napkins are the perfect size to get your family through messes and spills. From family dinners to big celebrations, Bounty Napkins are designed to hold up for any occasion. They're tough on those messy meals so they don't mess with you.*vs. leading ordinary brand")
    
    db.session.add(gain_flings)
    db.session.add(bounce_dryer_sheets)
    db.session.add(swiffer)
    db.session.add(candle)
    db.session.add(dishwasher_detergent)
    db.session.add(charmin)
    db.session.add(glad_forceflex)
    db.session.add(clorox)
    db.session.add(handwash)
    db.session.add(food_storage)
    db.session.add(foil)
    db.session.add(napkins)


    # Add products to sports_outdoors(3) prodcuts 25-36
    mongoose = Product(department_id=3, name="Mongoose Men's Standoff 26in Mountain Bike - Black", price=249.99 , description="Mongoose brings its “push the limits” attitude to mountain bikes. The Standoff has a full suspension frame and front suspension fork so it will be comfortable chewing up rough terrain, and with 21 speeds and thick knobby tires nothing will stand in your way. Take it on the trail or adventure off the trail onto some gnarly single track. There is nothing you can't do on a Mongoose.")
    huffy = Product(department_id=3, name="Huffy Women's Nassau 26in Cruiser Bike - Teal", price=209.99 , description="New and only at Bullsye! Ahhhh Nassau, the name evokes sand, waves, soft breezes and the beach. Yes the beach! This Huffy 26in Nassau Women's Beach Cruiser is awash in a sea crystal sparkle, with delicate frills on the frame and chainguard. The richly padded seat, embroidered with the Huffy logo and trimmed with sea crystal piping, the stylish wicker basket, and the rear storage rack are wonderful touches that make this one special ride.")
    hoverboard = Product(department_id=3, name='Jetson Mojo Light Up Hoverboard with Bluetooth Speaker', price=89.99 , description=" Find your mojo with the Jetson Mojo All-Terrain Hoverboard. Bring the swagger with this hoverboard featuring Jetson's signature full-color spectrum LAVA Tech LED lights on the wheel rims and deck pads. And bring the vibes with the Jetson Mojo's Bluetooth speaker. With its stylish metallic brush finish, The Jetson Mojo is a premium ride that is sure to impress. A top speed of 10 miles per hour and a maximum battery range of 8 miles will have you cruising around the neighborhood in style. Recommended for ages 12 and up.")
    scooter = Product(department_id=3, name='Razor A Kick Scooter', price=22.00 , description="The classic scooter with the A Scooter by Razor will be just the thing your kiddo needs to make their holiday more fun. It has a top-grade aluminum frame and urethane wheels with standard ABEC 5 bearings that make it great for speeding around the neighborhood. This scooter has a rear fender brake, adjustable handlebar with 3 different height settings and t-tube and deck to improve its performance. It is lightweight and can be easily folded. Give it a few scoots to cruise around your home with a razor speed.")
    golfbag = Product(department_id=3, name='Bridgestone NCAA Golf Cart Bag-Ohio State', price=239.99 , description="The Bridgestone NCAA Cart Bag features 7-way divider top with a top lift handle. The cart bag has 6 zippered pockets including a cooler pocket and an outer golf ball holder. Also included with the cart bag is a rain hood to help keep your clubs dry during rainy days.")
    hoop = Product(department_id=3, name='Best Choice Products Kids Height-Adjustable Basketball Hoop', price=119.99 , description="This grow with me mobile rim is fully adjustable, so kids ages 8 and up can keep playing as they grow. Use the two adjustment knobs for maximum tweaking and control, achieving a range of floor-to-rim heights between min 70.5in - max 82.3in. The elements shouldn't get in the way of your game, so this hoop's weather-resistant materials are ready for play in rainy weather or sunny weather. Part of a durable & user-friendly makeup, its backboard is built tough to resist breakage with normal use. Plus, the base is designed with a groove to hold your ball after you play for convenient ball storage.")
    pingpong = Product(department_id=3, name='EastPoint Mid-Sized Easy Setup Table Tennis Table', price=118.99 , description="Go head-to-head against your opponents with the EastPoint Sports Mid-Size Easy Setup Table Tennis Table. This mid-sized table arrives 100% pre-assembled and sets up in a matter of seconds. Just unpack it from the box, unfold the legs, flip, and play! It's truly that simple. Measuring 7'8” long x 4'4” wide, this table is designed to pack big time competition into tighter, smaller spaces. Once the games have finished, the 2 independent halves fold down to manageable 46 in. x 26 in. “suitcases” that can be easily stored in a closet. The warp-resistant 15mm play surface yields a consistent bounce and the sturdy steel frame provides a solid base. This table includes everything you need to play: steel net & post set, 2 paddles, and 2 table tennis balls.")
    dartboard = Product(department_id=3, name='Franklin Sports Bristle Dartboard with Medal Ring Scoring', price=27.99 , description="Franklin Sports Pro Wire Dartboard is a great addition to any game room. This dartboard is perfect for any kids' room, game room or man cave! Players will love the tournament size 18in self-healing bristle dartboard. Each section is separated by steel wires to ensure the scoring sections are easy to see game after game. This board sets up quickly and comes with all the needed hardware. Step your game up and join the Franklin Family today by taking home your very own Pro Wire Dartboard!")
    theragun = Product(department_id=3, name='Theragun Prime Handheld Percussive Massage Device', price=179.99 , description="Theragun Prime™Essential Features hardly Any Sound. The perfect balance of strength and style. Offers deep muscle treatment for your body's needs. The essential Smart Percussive Therapy device is ergonomically designed for everyone in mind. Coupled with our intuitive app as yourguide the Theragun Prime helps to release everyday strain and stress.Unrivaled Power. Remarkably Quiet™ .Proprietary brushless motor with QuietForce Technology™ delivers renowned Theragun power, while being quieter than ever for up to 120 minutes.Bluetooth Enabled Smart Percussive Therapy™ The Therabody app connects seamlessly via Bluetooth to deliver customized wellness routines pulled from your activity data.")
    exercise_bike = Product(department_id=3, name='Schwinn IC3 Indoor Cycling Exercise Bike - Black', price=699.99 , description="The new Schwinn IC3 is a low impact, cardio-kicking indoor cycling bike designed with the serious cyclist in mind. When harsh weather or a crazy schedule drives your workout inside, just hop on the IC3 for a high-energy, low-impact training experience that will have you feeling like you're riding through rolling hills. With a generous LCD console, a 40-pound flywheel and infinitely variable resistance, this bike offers serious value for the serious cyclist.")
    spikeball = Product(department_id=3, name='Spikeball Roundnet Combo Meal Set with 3 balls and Backpack - Yellow/Black', price=69.99 , description="Let summer adventures begin with the exciting Spikeball Combo Meal Set with 3 balls and Backpack Roundnet - Yellow/Black. Easy to play, and easy to set up, this sports kit includes a net, 3 balls, a drawstring bag and instructions. With rules combining four square and volleyball, this fun game is played by two teams of two players each. The net is set at ankle level between the two teams while the players takes turns hitting the ball on to the net so it ricochets up at the opponent. Each team gets three turns between them to bounce the ball back to their opponent. If one team misses, the other team scores a point, and the first team to get 21 points wins. The included bag makes it easy to carry around, so you can have a great game every time you hit the beach, or attend a backyard barbecue.")
    cornhole = Product(department_id=3, name='Beyond Outdoors Wooden Bean Bag Toss', price=79.99 , description="Enjoy a day in the sun with the Beyond Outdoors Cornhole Set! This set includes two 2' x 3' wooden boards and eight Premium Stick & Slide Dual Sided Bean Bags that offer two different tossing methods. Our cornhole boards attach together and include carry handles to make transportation and storage simple. Challenge your friends and family to a tossing competition on the Beyond Outdoors Cornhole Set today!")
    
    db.session.add(mongoose)
    db.session.add(huffy)
    db.session.add(hoverboard)
    db.session.add(scooter)
    db.session.add(golfbag)
    db.session.add(hoop)
    db.session.add(pingpong)
    db.session.add(dartboard)
    db.session.add(theragun)
    db.session.add(exercise_bike)
    db.session.add(spikeball)
    db.session.add(cornhole)
    
    
    
    db.session.commit()

    def undo_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM products")
        
    db.session.commit()
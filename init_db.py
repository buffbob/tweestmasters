from tweestmaster import db

import tweestmaster.models as tm


# add tables
db.create_all()
# add admin, site_forum and first Article
article_content = """For many years, people had suspected the mountains in present-day Colorado contained numerous rich gold deposits. In 1835, French trapper Eustace Carriere lost his party and ended up wandering through the mountains for many weeks. During those weeks he found many gold specimens which he later took back to New Mexico for examination. Upon examination, they turned out to be "pure gold". But when he tried to lead an expedition back to the location of where he found the gold, they came up short because he could not quite remember the location.[3]
In 1849 and 1850, several parties of gold seekers bound for the California Gold Rush panned small amounts of gold from various streams in the South Platte River valley at the foot of the Rocky Mountains. The Rocky Mountain gold failed to impress or delay men with visions of unlimited wealth in California, and the discoveries were not reported for several years.[4]
As the hysteria of the California Gold Rush faded, many discouraged gold seekers returned home. Rumors of gold in the Rocky Mountains persisted and several small parties explored the region. In the summer of 1857, a party of Spanish-speaking gold seekers from New Mexico worked a placer deposit along the South Platte River about 5 miles (8 kilometers) above Cherry Creek, now part of metropolitan Denver.[1]
Sluicing for gold, photo by the U.S. Geological and Geographic Survey of the Territories. (1874–1879) Photographer: William Henry Jackson
William Greeneberry "Green" Russell was a Georgian who worked in the California gold fields in the 1850s. Russell was married to a Cherokee woman, and through his connections to the tribe, he heard about an 1849 discovery of gold along the South Platte River. Green Russell organized a party to prospect along the South Platte River, setting off with his two brothers and six companions in February 1858. They rendezvoused with Cherokee tribe members along the Arkansas River in present-day Oklahoma and continued westward along the Santa Fe Trail. Others joined the party along the way until their number reached 107.[4]
Upon reaching Bent's Fort, they turned to the northwest, reaching the confluence of Cherry Creek and the South Platte on May 23. The site of their initial explorations is in present-day Confluence Park in Denver. They began prospecting in the river beds, exploring Cherry Creek and nearby Ralston Creek but without success. In the first week of July 1858, Green Russell and Sam Bates found a small placer deposit near the mouth of Little Dry Creek that yielded about 20 troy ounces (622 grams) of gold, the first significant gold discovery in the Rocky Mountain region. The site of the discovery is in the present-day Denver suburb of Englewood, just north of the junction of U.S. Highway 285 and U.S. Highway 85.[4]
""".replace("\n","")
article_content2 = """Nature got it right with the cranes. They have been around since the Eocene, which ended 34 million years ago. They are among the world’s oldest living birds and one of the planet’s most successful life-forms, having outlasted millions of species (99 percent of species that ever existed are now extinct). The particularly successful sandhill crane of North America has not changed appreciably in ten million years. There are 15 Gruidae species, and in all the human cultures that experience the birds, they are revered.
In my travels I have encountered cranes on three continents. Tibet, November 1995: Driving along the Yarlung River, we spot a flock of black-necked cranes in a marshy flat, but when we try to sneak closer on foot with our cameras, they see us from a long distance and, slowly lifting themselves up into the air on their enormous wings, take off. There are only 6,000 or so black-necks. These are making their way south, to spend the winter foraging on agricultural residue in Bhutan. Three hundred black-necks return each December to Phobjikha Valley, where in the morning and evening, as they take off to eat and dance and return for the night, they circle repeatedly around a monastery called Gangtey Gompa. The local Bhutanese believe them to be reincarnations of departed monks, and have for centuries performed elegant crane dances, tilting and sweeping long white wings attached to their arms. Cranes are the Bolshoi of animal dance. They dance at the drop of a hat, for all kinds of reasons, not just courtship.
Neolithic peoples in Turkey in 6500 B.C. imitated the dances of cranes as part of marriage rituals. Dance is one thing cranes are credited by many societies with giving us. Another is language, perhaps because they are so vocal and a single crane’s calls, amplified by its saxophone-shaped trachea—the windpipe in its long neck—can carry a mile. And unlike geese, with their disciplined, purposeful vees, cranes fly in loose, drifting, chimeric lines that are constantly, kaleidoscopically coming apart and forming, the ancient Greeks imagined, many letters. Crane hieroglyphs were applied to the Temples of Karnak 4,000 years ago.
In 1990 my wife and I were married in her village in southwestern Uganda. The festivities went on for three days, and all the while a couple of dozen gray-crowned cranes, with regal bonnets of sun-shot yellow feathers, were pecking and padding around in the adjacent savanna. The gray-crowned crane is my wife’s clan totem, so their presence was auspicious. Once common all over East Africa, this species is taking a terrible toll from local poachers who are selling them to the international pet trade. Only 30,000 gray-crowned cranes are left in all of Africa.
The sandhill cranes of North America are the most abundant crane species. Migrating sandhills come in three basic sizes—greater, lesser and the mid-size Canadian. I’ve seen the resident sandhills in Florida, three of them pecking for worms on a lawn outside Orlando, and several members of another resident population in Mississippi, which has just 25 breeding pairs. The Eastern population has rebounded dramatically from near extinction in the 1930s and is now up to more than 80,000. I saw a couple of big sandhills on the north bank of the St. Lawrence River in eastern Quebec, just above the mouth of the Saguenay River, a few summers ago.
Every year 400,000 to 600,000 sandhill cranes—80 percent of all the cranes on the planet—congregate along an 80-mile stretch of the central Platte River in Nebraska, to fatten up on waste grain in the empty cornfields in preparation for the journey to their Arctic and subarctic nesting grounds. This staging is one of the world’s great wildlife spectacles, on a par with the epic migrations of the wildebeest and the caribou. It takes place in three waves of four to five weeks each, beginning in mid-February and ending in mid-April, during which birds that arrive emaciated from wintering grounds in Texas, New Mexico, Arizona and Chihuahua, Mexico, gain 20 percent of their body weight.
It usually peaks in the last week of March, which was the case in 2013. Wildlife photographer extraordinaire Melissa Groo and I hit it just right.
""".replace("\n","")
article_content3 = """We recently wrote to the NFL Commissioner and Team Owners with a specific concern about plastic waste and pollution and a request that the NFL be an active part in ending what has become a pollution epidemic.  Plastic pollution has significant impacts to the ocean in areas such as South Florida where the NFL will host Super Bowl LIV in 2020.  As NFL fans and members of NFL team communities who are actively involved in ocean and environmental issues, we request that the NFL end licensing of team logos on non-recyclable, non-durable expanded polystyrene (EPS) foam coolers that create waste to landfills and pollution to the ocean.
Just as the NFL has improved the technology of helmets to protect the health of players over the last decades, we request that the NFL now license only to reusable, non-polluting coolers to protect the health of the oceans, ecosystems and many species suffering from plastic pollution. The disposable design of EPS foam coolers is as outdated as leather football helmets.
The Miami Super Bowl LIV Host Committee recently announced the launch of the Ocean to Everglades (O2E) campaign aimed “to reduce the environmental impact around Super Bowl events and promote sustainability around the unique confluence of ocean and land-based issues found in South Florida”. Promotion of EPS foam coolers is counterproductive to the O2E initiative because EPS foam is described as the biggest plastic pollution problem by a marine biologist in Key Largo, Florida who volunteers at monthly coastline cleanups.  “We always go to the same spot and no matter what time of the year, Styrofoam coolers and just chunks of Styrofoam are always there,” she said. Marine life experts in Jupiter, Florida say ocean trash is threatening the lives of sea turtles.  In the last year alone, over 35,000 foam pieces were collected on a small 9.5 mile stretch of beach they patrol. Up north in Baltimore Harbor, Maryland, Mr. Trash Wheel collected 1,028,000 Styrofoam containers in five years. This has led the State of Maryland to pass a statewide ban on EPS foam containers.
The NFL has licensed team logos for imprinting on EPS foam coolers for decades. The coolers are sold in grocery and convenience stores across the United States (U.S.) and are designed to be disposed after only a few uses.  The light weight, non-durable nature of EPS foam leads to cooler breakage through wear and tear experienced in normal use. The old-fashioned disposable design creates non-recyclable plastic waste that must be sent to landfills and is now understood to create plastic pollution to the ocean.  Experts estimate that 300,000 metric tonnes of plastic waste from the United States (U.S.) pollute the ocean every year, which is about 65 dump trucks of plastic waste per day. Disposable EPS foam coolers contribute to this plastic pollution that is a blight in our cities and on our landscapes and harms our rivers and oceans. 
Plastic waste and pollution are a burden to cities and communities to pay for waste disposal, landfill expansion and pollution cleanup. Over 200 U.S. cities and communities have banned EPS foam containers because of the costs to dispose of the plastic waste and its many harms to the environment. Sales of NFL EPS foam coolers are now illegal in New York City, Nassau County, Maine, Maryland, San Francisco, San Diego and several cities in the Los Angeles area. Use of NFL EPS foam coolers is illegal in Miami-Dade County Parks and Beaches. More U.S. cities and states are considering EPS foam container bans in 2019. Recycling of EPS foam is not a viable, realistic option in the U.S. due to the high cost of collection, cleaning and processing. As a result, only about 1% of EPS foam containers and packaging was recycled in the U.S. in 2017.
Major brand companies, including McDonald’s, Dunkin Donuts, Baskin Robbins and Wendy’s, have stopped distributing EPS foam consumer products to remove their valuable logos from the environmentally harmful EPS foam products.
""".replace("\n","")

u1 = tm.User(username="Admin", email='admin@tweestmasters.com', password='admin')
site_forum = tm.Forum(name='Master', description = "tweestmasters home forum. Striving to be our best.", leader_id=1)
nobody = tm.Forum(name='Long live Manatees', description = "A site devoted to environmentalists", leader_id=2)

# create article pictures for article one
ap1 = tm.ArticlePicture(uri="index1.jpg", article_id=1)
ap2 = tm.ArticlePicture(uri="index2.jpg", article_id=1)
ap3 = tm.ArticlePicture(uri="index3.jpg", article_id=1)
# create article pictures for article two
ap4 = tm.ArticlePicture(uri="index4.jpg", article_id=2)
ap5 = tm.ArticlePicture(uri="index5.jpg", article_id=2)
ap6 = tm.ArticlePicture(uri="index6.jpg", article_id=2)

# create article pictures for article three
ap7 = tm.ArticlePicture(uri="index7.jpg", article_id=3)
ap8 = tm.ArticlePicture(uri="index8.jpg", article_id=3)
ap9 = tm.ArticlePicture(uri="index9.jpg", article_id=3)



a1 = tm.Article(title='Days of Doom', content=article_content + article_content, forum_id=1, user_id=1)
a2 = tm.Article(title='I saw the light- it was bright', content=article_content2, forum_id=1, user_id=1)
a3 = tm.Article(title="Man's Greatest Invention?... is killing us!", content=article_content3, forum_id=2, user_id=2)
# now add 2 more users
u2 = tm.User(username="BuffBob", email="lastgulch@gmail.com", password="password")
u3 = tm.User(username="Squirrel", email="squirrel@gmail.com", password="password")
db.session.add(ap1)
db.session.add(ap2)
db.session.add(ap3)
db.session.add(ap4)
db.session.add(ap5)
db.session.add(ap6)
db.session.add(ap7)
db.session.add(ap8)
db.session.add(ap9)


db.session.add(u1)
db.session.add(site_forum)
db.session.add(nobody)
db.session.add(a1)
db.session.add(a2)
db.session.add(a3)
db.session.add(u2)
db.session.add(u3)
db.session.commit()

#todo:  add all users to site forum, add users 2,3 to nobody


# u2 will write 2 tweests on
t1_content="""when i was young, things were not so rosy either. we used to practice bomb drills 
in our classrooms. and Halloween was filled with stories of needles in apples""".replace('\n','')

t2_content="""things actually have gone down hill consederable. i used to walk my dog to school 
and it would wait until lunch for me. Then he would share some love and wait by my bike until the 
bell rang. tail would start wagging and assumming i was not summoned to the office I would be at 
her side within minutes.""".replace('\n','')
t1 = tm.Tweest(title="Not so much doom- please! It has been much worse in the recent past!", content=t1_content,user_id=2,forum_id=1,article_id=1)
t2 = tm.Tweest(title="This is Just the Beginning of a Cascade!", content=t2_content,user_id=2,forum_id=1,article_id=1)
r1 = tm.Review(score=55,content="is this as good as you can do. start with spellchecker and move on to the dictionary...", tweest_id=3, forum_id=2,user_id=3)

db.session.add(t1)
db.session.add(t2)
db.session.add(r1)
db.session.commit()

print('shit')







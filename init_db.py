from tweestmaster import db, bcrypt,create_app

import tweestmaster.models as tm
import secrets
# admin pass
admin_pass = 'passpass'
# hashed pass
# pwh = bcrypt.generate_password_hash(admin_pass)

# add admin, site_forum and first Article
article_content1 = """For many years, people had suspected the mountains in present-day Colorado contained numerous rich gold deposits. In 1835, French trapper Eustace Carriere lost his party and ended up wandering through the mountains for many weeks. During those weeks he found many gold specimens which he later took back to New Mexico for examination. Upon examination, they turned out to be "pure gold". But when he tried to lead an expedition back to the location of where he found the gold, they came up short because he could not quite remember the location.
In 1849 and 1850, several parties of gold seekers bound for the California Gold Rush panned small amounts of gold from various streams in the South Platte River valley at the foot of the Rocky Mountains. The Rocky Mountain gold failed to impress or delay men with visions of unlimited wealth in California, and the discoveries were not reported for several years.
As the hysteria of the California Gold Rush faded, many discouraged gold seekers returned home. Rumors of gold in the Rocky Mountains persisted and several small parties explored the region. In the summer of 1857, a party of Spanish-speaking gold seekers from New Mexico worked a placer deposit along the South Platte River about 5 miles (8 kilometers) above Cherry Creek, now part of metropolitan Denver.
Sluicing for gold, photo by the U.S. Geological and Geographic Survey of the Territories. (1874–1879) Photographer: William Henry Jackson
William Greeneberry "Green" Russell was a Georgian who worked in the California gold fields in the 1850s. Russell was married to a Cherokee woman, and through his connections to the tribe, he heard about an 1849 discovery of gold along the South Platte River. Green Russell organized a party to prospect along the South Platte River, setting off with his two brothers and six companions in February 1858. They rendezvoused with Cherokee tribe members along the Arkansas River in present-day Oklahoma and continued westward along the Santa Fe Trail. Others joined the party along the way until their number reached 107.
Upon reaching Bent's Fort, they turned to the northwest, reaching the confluence of Cherry Creek and the South Platte on May 23. The site of their initial explorations is in present-day Confluence Park in Denver. They began prospecting in the river beds, exploring Cherry Creek and nearby Ralston Creek but without success. In the first week of July 1858, Green Russell and Sam Bates found a small placer deposit near the mouth of Little Dry Creek that yielded about 20 troy ounces (622 grams) of gold, the first significant gold discovery in the Rocky Mountain region. The site of the discovery is in the present-day Denver suburb of Englewood, just north of the junction of U.S. Highway 285 and U.S. Highway 85.
""".replace("\n","")
article_content2 = """Nature got it right with the cranes. They have been around since the Eocene, which ended 34 million years ago. They are among the world’s oldest living birds and one of the planet’s most successful life-forms, having outlasted millions of species (99 percent of species that ever existed are now extinct). The particularly successful sandhill crane of North America has not changed appreciably in ten million years. There are 15 Gruidae species, and in all the human cultures that experience the birds, they are revered.
In my travels I have encountered cranes on three continents. Tibet, November 1995: Driving along the Yarlung River, we spot a flock of black-necked cranes in a marshy flat, but when we try to sneak closer on foot with our cameras, they see us from a long distance and, slowly lifting themselves up into the air on their enormous wings, take off. There are only 6,000 or so black-necks. These are making their way south, to spend the winter foraging on agricultural residue in Bhutan. Three hundred black-necks return each December to Phobjikha Valley, where in the morning and evening, as they take off to eat and dance and return for the night, they circle repeatedly around a monastery called Gangtey Gompa. The local Bhutanese believe them to be reincarnations of departed monks, and have for centuries performed elegant crane dances, tilting and sweeping long white wings attached to their arms. Cranes are the Bolshoi of animal dance. They dance at the drop of a hat, for all kinds of reasons, not just courtship.
Neolithic peoples in Turkey in 6500 B.C. imitated the dances of cranes as part of marriage rituals. Dance is one thing cranes are credited by many societies with giving us. Another is language, perhaps because they are so vocal and a single crane’s calls, amplified by its saxophone-shaped trachea—the windpipe in its long neck—can carry a mile. And unlike geese, with their disciplined, purposeful vees, cranes fly in loose, drifting, chimeric lines that are constantly, kaleidoscopically coming apart and forming, the ancient Greeks imagined, many letters. Crane hieroglyphs were applied to the Temples of Karnak 4,000 years ago.
In 1990 my wife and I were married in her village in southwestern Uganda. The festivities went on for three days, and all the while a couple of dozen gray-crowned cranes, with regal bonnets of sun-shot yellow feathers, were pecking and padding around in the adjacent savanna. The gray-crowned crane is my wife’s clan totem, so their presence was auspicious. Once common all over East Africa, this species is taking a terrible toll from local poachers who are selling them to the international pet trade. Only 30,000 gray-crowned cranes are left in all of Africa.
The sandhill cranes of North America are the most abundant crane species. Migrating sandhills come in three basic sizes—greater, lesser and the mid-size Canadian. I’ve seen the resident sandhills in Florida, three of them pecking for worms on a lawn outside Orlando, and several members of another resident population in Mississippi, which has just 25 breeding pairs. The Eastern population has rebounded dramatically from near extinction in the 1930s and is now up to more than 80,000. I saw a couple of big sandhills on the north bank of the St. Lawrence River in eastern Quebec, just above the mouth of the Saguenay River, a few summers ago.
Every year 400,000 to 600,000 sandhill cranes—80 percent of all the cranes on the planet—congregate along an 80-mile stretch of the central Platte River in Nebraska, to fatten up on waste grain in the empty cornfields in preparation for the journey to their Arctic and subarctic nesting grounds. This staging is one of the world’s great wildlife spectacles, on a par with the epic migrations of the wildebeest and the caribou. It takes place in three waves of four to five weeks each, beginning in mid-February and ending in mid-April, during which birds that arrive emaciated from wintering grounds in Texas, New Mexico, Arizona and Chihuahua, Mexico, gain 20 percent of their body weight.
It usually peaks in the last week of March, which was the case in 2013. Wildlife photographer extraordinaire Melissa Groo and I hit it just right.
""".replace("\n","")

article_content3 = """This New York Times dispatch is more than a hundred and fifty years old, and yet it sounds surprisingly modern: elephants, the paper warned in 1867, were in grave danger of being 'numbered with extinct species' because of humans' insatiable demand for the ivory in their tusks. Ivory, at the time, was used for all manner of things, from buttonhooks to boxes, piano keys to combs. But one of the biggest uses was for billiard balls. Billiards had come to captivate upper-crust society in the United States as well as in Europe. Every estate, every mansion had a billiards table, and by the mid-1800s, there was growing concern that there would soon be no more elephants left 
to keep the game tables stocked with balls. The situation was most dire in Ceylon, source of the ivory that made the best billiard balls. There, in the northern part of the island, the Times reported, 'upon the reward of a few shillings per head being offered by the authorities, 3,500 pachyderms were dispatched in less than three years by the natives.' All told, at least one million pounds of ivory were consumed each year, sparking fears of an ivory shortage. 'Long before the elephants are no more and the mammoths used up,' the Times hoped, 'an adequate substitute may [be] found.'
Ivory wasn't the only item in nature's vast larder that was starting to run low. The hawksbill turtle, that unhappy supplier of the shell used to fashion combs, was becoming scarcer. Even cattle horn, another natural plastic that had been used by American comb makers since before the Revolutionary War, was becoming less available as ranchers stopped dehorning their cattle.
In 1863, so the story goes, a New York billiards supplier ran a newspaper ad offering 'a handsome fortune,' ten thousand dollars in gold, to anyone who could come up with a suitable alternative for ivory. John Wesley Hyatt, a young journeyman printer in Upstate New York, read the ad and decided he could do it. Hyatt had no formal training in chemistry, but he did have a knack for invention—at the age of twenty-three, he'd patented a knife sharpener. Setting up in a shack behind his home, he began experimenting with various combinations of solvents and a doughy mixture made of nitric acid and cotton. (That nitric 
acid–cotton combination, called guncotton, was daunting to work with because it was highly flammable, even explosive. For a while it was used as a substitute for gunpowder until producers of it got tired of having their factories blow up.)   
As he worked in his homemade lab, Hyatt was building on decades of invention and innovation that had been spurred not only by the limited quantities of natural materials but also by their physical limitations. The Victorian era was fascinated with natural plastics such as rubber and shellac. As historian Robert Friedel pointed out, they saw in these substances the first hints of ways to transcend the vexing limits of wood and iron and glass. Here were materials that were malleable but also amenable to being hardened into a final manufactured form. In an era already being rapidly transformed by  
industrialization, that was an alluring combination of qualities—one hearkening to both the solid past and the tantalizingly fluid future. Nineteenth-century patent books are filled with inventions involving combinations of cork, sawdust, rubbers, and gums, even blood and milk protein, all designed to yield materials that had some of the qualities we now ascribe to plastic. These plastic prototypes found their way into a few decorative items, such as daguerreotype cases, but they were really only intimations of things to come. The noun plastic had not yet been coined—and wouldn't be until the early twentieth century—but we were already dreaming in plastic. 
While celluloid would prove a wonderful substitute for ivory, Hyatt apparently never collected the ten-thousand-dollar prize. Perhaps that's because celluloid didn't make very good billiard balls—at least not at first. It lacked the bounce and resilience of ivory, and it was highly volatile. The first balls Hyatt made produced a loud crack, like a shotgun blast, when they knocked into each other. One Colorado saloonkeeper wrote Hyatt that 'he didn't mind, but every time the balls collided, every man in the room pulled a gun.' And a new age was begining.
""".replace("\n", "")

# u2 will write 2 tweests on
# t1_content="""In the early seventies while attending public elementary school, myself and fellow students participated in school bomb drills.
#
# If memory serves correctly, we practiced sitting under desks with arms folded over our heads. I think we never broached the subject of radiation. But the fear was of nuclear weapons not conventional.
#
# There were seemingly vivid accounts every Halloween about contaminated treats. Believe it or not people used to give fruit and homemade treats out for Halloween. Several
#
# stories of needles in apples and razors in rice crispy treats. During this period there were several well publicized taintings. People putting dangerous substances in products at grocery stores. Remember the Chicago Tylenol Murders, a total of seven people died in the original poisonings, with several more deaths in subsequent copycat crimes.
# """.replace('\n','')

t1_content = """Gold is the heaviest substance that you will find in a creek or river, and because of this it is somewhat predictable in the way that it deposits itself in a waterway. It will form in what is known as “paystreaks,” or lines of gold.

These paystreaks will settle down through the sand and gravel and sit directly on bedrock. They will be richest down in the cracks and crevices of the bedrock. 

High water during the spring will add more gold to these paystreaks. They are constantly refreshed by gold that erodes from the hills and feed into the river. 

Inside bends of a river where water slows is the best known place to find gold deposits in paystreaks, but they also form in concentrations behind boulders, logjams, under waterfalls, or anywhere that the velocity of water slows. 
In recent years, suction dredges were the best way to efficiently mine the gold paystreaks in a river due to their ability to process lots of gravel from the riverbed. Dredges are still the best tool for the job, but permitting and regulations have gotten difficult in recent years. Many prospectors are now limited to using sluices and highbankers in many states. 
""".replace('\n', '')

t2_content="""I have the fondest memory of my childhood dog. Cleo was a young energetic white german shepard and she had no one to play with while I was at school.  
She was very familiar with my school. A common activity was to take her to the playground after school. Sometimes she would chase me and my friends as 
we rode the 1/2 mile to school on our bikes. Other times she would pull me on my skateboard. She learned to use most of playground equipment. Most amazing 
to me was her ability to climb the monkey bars. Playground equipment- there is a story for another day. 
Dogs on leashes- are you kidding me. On school days she was too energetic to be inside all day so my mom had no choice but let her out. And when Cleo tasted 
freedom it was off to school where she often would sit by my bike. Other times she would actively look for me. I got calls for a while from the office to take 
her home. But it seems that after missing too much time the school just let her be.
""".replace('\n','')

t3_content = """Admit it. You’ve always wanted the ability to magically befriend wild animals, like the Beastmaster or some Disney princess. But while most of us can only dream of communicating with other creatures, Gabi Mann is pretty tight with the animal kingdom. This eight-year-old from Seattle is best friends with a flock of crows. In fact, they even give her gifts. 

This incredibly odd friendship began when she was just four and would constantly spill her food. The neighborhood birds took note, and they were soon watching Gabi every time she stepped outside, just in case she dropped some sort of tasty treat. As Gabi grew older, she intentionally started sharing her lunch with the crows, and it was soon an everyday thing. With her mother’s help, Gabi kept a bird feeder full of peanuts and regularly tossed dog food onto the lawn. 

And the crows started leaving presents. Once, it was an earring. Another time, it was a broken lightbulb. They left a button, a paper clip, a rock, and a Lego piece. Each time, the birds would gobble up the food and then leave a token of their appreciation. Soon, Gabi was collecting their little gifts, bagging each item and marking every present with the date, description, and the location where she found it. And even though she really loves the rusty screw and the black zipper, her favorite gift is a little plastic heart. As she told the BBC, “It’s showing me how much they love me.”""".replace('\n','')



t4_content = """Jim Eggers has an anger problem. Jim once dented a woman’s car with his first. He poured steaming hot coffee on somebody’s head. He’s even threatened to kill people. During the heyday of the Catholic Church sex scandal, Eggers was convinced the local archbishop was covering up pedophilia (he wasn’t) and threatened to murder the man. 

Jim suffers from bipolar disorder with psychotic tendencies. Back in the day, you did not want to get on his bad side. However, he’s doing a whole lot better these days, totally thanks to Sadie, an African gray parrot. 

In 2005, shortly after the Archbishop Incident, Jim rescued Sadie from a bad environment. Her previous owner was just a kid and didn’t take care of the poor bird. Incredibly stressed, Sadie started tearing her own feathers out, but fortunately, Jim was a big animal lover and nursed the bird back to health. And Sadie returned the favor. 

Oftentimes, when Jim felt his mood starting to swing, when his vision blurred and his whole entire body started to quiver, right before he went into rage monster mode, he would pace back and forth in his apartment, muttering things like, “It’s okay, Jim. Calm down, Jim. You’re all right, Jim.” Usually, it helped him get a lid on all that anger. One day, as he started to hulk out, Sadie started squawking, “It’s okay, Jim. Calm down, Jim. You’re all right, Jim.” 

Sadie’s words were incredibly soothing, so Jim gave the parrot treats every time she calmed him down. And Sadie developed some sort of sixth sense. According to Jim, she started to sense his mood swings before he even got angry. Somehow, she could tell he was growing irritated, and she’d whisper, “Calm down, Jim.” 

Ever since then, Jim has carried Sadie wherever he goes. He even bought a special purple backpack that carries a cage. Whenever he needs to go to the store or ride the bus, he takes Sadie along, bumping against his back, and if something ever ticks him off, she’s right there, ready to squawk, “It’s okay, Jim.”""".replace('\n','')


t5_content = """Tom the turkey was a local legend in Chilmark, Massachusetts, a little town on Martha’s Vineyard. His tragic tale begins in 2006, when young orphan Tom was injured by a hawk. Fortunately, he was saved by a loving couple, Jonathan and Linda Haar. Though they never adopted Tom as a pet, they healed his wounds and fed him regularly. Soon, Tom was hanging around their house all the time, and the couple fell in love with this ugly bird. 

The rest of the neighbors hated Tom’s guts, probably because he was the scariest turkey in history. He regularly attacked other people, and like Cujo with a comb, he’d trap people in their cars and circle their vehicles, daring his victims to step out. Even worse, sometimes he’d whip up a mad turkey mob and attack unsuspecting people while his gang crowded around. 

Terrified neighbors parked close to their front doors so they could make a quick dash to safety. Some carried brooms or bats when they went outside. No one was safe from the terrible Tom, except Jonathan and Linda, who didn’t know how foul their fowl had become. 

Things came to a head when a deliverywoman called the cops, complaining that a wild turkey was menacing the streets. When two officers arrived, Tom wasn’t intimidated. Instead, he attacked the cops, forcing one of the officers to jump on his car. The second officer pulled out his pistol and fired twice, wounding the turkey. Tom dashed off, and the police chased after him, guns blazing. Tom was finally dead. 

Jonathan ran up, screaming and shouting. He’d loved that bird. In fact, he was so angry that he slugged one of the cops in the face. Jonathan was hauled into jail, and the story became a big-time scandal. People who didn’t live in Tom’s territory wrote to the newspapers, complaining about the cop’s excessive use of force. One paper ran a cartoon of a stupid-looking turkey dressed up as a police officer. For weeks, it’s all anyone talked about. 

Not much happens in Chilmark, Massachusetts. 

Six months, $30,000 in legal fees, and several dropped charges later, Jonathan was finally released . . . and so was Tom. The police had kept his bullet-ridden body in a freezer as evidence, so Tom was probably coated with frost. Brokenhearted, Jonathan and Linda buried Tom in their yard, complete with a tombstone that read: “Tom the Turkey. He died as he lived.”""".replace("\n", "")



####################################################################
app= create_app()

with app.app_context():
    # add tables for sqlite  ## not needed for mysql after "flask db upgrade"
    # db.create_all()
    #  db.session.commit()

    u1 = tm.User(username="Admin", email='admin@tweestmasters.com', password=admin_pass)
    # now add 2 more users
    u2 = tm.User(username="BuffBob", email="lastgulch@gmail.com", password="password")
    u3 = tm.User(username="Squirrel", email="squirrel@gmail.com", password="password")
    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.commit()
    site_forum = tm.Forum(name='Master', description="Tweestmasters' home forum.", leader_id=1)

    # a second forum and add the Admin as a user
    nobody = tm.Forum(name='Mother Nature bats last', description="A site devoted the environment", leader_id=2)
    db.session.add(site_forum)
    db.session.add(nobody)
    db.session.commit()
    # and add them to membership in the  forums
    site_forum.users.append(u1)
    nobody.users.append(u1)

    # and add them to membership in the Master forum
    site_forum.users.append(u2)
    site_forum.users.append(u3)
    nobody.users.append(u2)

    db.session.commit()


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

    a1 = tm.Article(title='Glory Days', content=article_content1, forum_id=1, user_id=1)
    a2 = tm.Article(title="Nature's great indulgences", content=article_content2, forum_id=1, user_id=1)
    a3 = tm.Article(title="Man's Greatest Invention?", content=article_content3, forum_id=2,
                    user_id=2)


    db.session.add(ap1)
    db.session.add(ap2)
    db.session.add(ap3)
    db.session.add(ap4)
    db.session.add(ap5)
    db.session.add(ap6)
    db.session.add(ap7)
    db.session.add(ap8)
    db.session.add(ap9)

    db.session.add(a1)
    db.session.add(a2)
    db.session.add(a3)

    db.session.commit()


    t1 = tm.Tweest(title="Seams Reasonable", content=t1_content,
                   user_id=2, forum_id=1, article_id=1)
    t2 = tm.Tweest(title="My best friend!", content=t2_content, user_id=1, forum_id=1,
                   article_id=1)
    t3 = tm.Tweest(title="Odd Friends", content=t3_content, user_id=2, forum_id=1, article_id=2)

    db.session.add(t1)
    db.session.add(t2)
    db.session.add(t3)

    t4 = tm.Tweest(title="Angry Bird", content=t4_content, user_id=3, forum_id=1, article_id=2)
    t5 = tm.Tweest(title="Tom the Turkey", content=t5_content, user_id=1, forum_id=1, article_id=2)

    db.session.add(t4)
    db.session.add(t5)

    db.session.commit()

print("wow, db loaded!")



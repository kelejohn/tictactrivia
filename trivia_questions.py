import random


def select_question(category):

    trivia = [ ]

    if category == "Pop Culture":
        trivia = [
                {
                    'question': 'Who is the oldest Kardashian sister?',
                    'answers': ['A. Kim', 'B. Khloe', 'C. Kourtney', 'D. Kendall'],
                    'correct_answer': 'C'
                },
                {
                    'question': "5 years after Friends ended, Jennifer Aniston made her return to TV on what show?",
                    'answers': ['A. The Morning Show', 'B. Big Little Lies', 'C. The Crown', 'D. The Handmaid\'s Tale'],
                    'correct_answer': 'A'
                },
                {
                    'question': "Which artist made history in 2020 as the youngest winner of the Grammys' four main categories?",
                    'answers': ['A. Ariana Grande', 'B. Taylor Swift', 'C. Billie Eilish', 'D. Justin Bieber'],
                    'correct_answer': 'C'
                },
                {
                    'question': "What year did Keeping Up with the Kardashians first premiere?",
                    'answers': ['A. 2005', 'B. 2006', 'C. 2007', 'D. 2008'],
                    'correct_answer': 'C'
                },
                {
                    'question': "Who was the first African-American man to achieve EGOT status?",
                    'answers': ['A. Quincy Jones', 'B. John Legend', 'C. Denzel Washington', 'D. Jamie Foxx'],
                    'correct_answer': 'B'
                },
                {
                    'question': "What was Dwayne 'The Rock' Johnson's first movie in a lead role?",
                    'answers': ['A. The Mummy Returns', 'B. Doom', 'C. The Rundown', 'D. The Scorpion King'],
                    'correct_answer': 'D'
                }
            ]

    elif category == "Literature":
        trivia = [
        {
            'question': 'Who wrote "To Kill a Mockingbird"?',
            'answers': ['A. Ernest Hemingway', 'B. Harper Lee', 'C. J.K. Rowling', 'D. George Orwell'],
            'correct_answer': 'B'
        },
        {
            'question': "A young boy takes a train to the North Pole on Christmas Eve in what classic 1985 children's book by Chris Van Allsburg?",
            'answers': ['A. Frosty The Snowman', 'B. The Polar Express', 'C. The Grinch Who Stole Christmas',
                        'D. Rudolph the Red-Nosed Reindeer'],
            'correct_answer': 'B'
        },
        {
            'question': "In the classic 1957 children's book, 'How the Grinch Stole Christmas,' what is the name of the town the Grinch steals holiday presents and decorations from?",
            'answers': ['A. Whoville', 'B. Christmas Town', 'C. Merryville', "D. Santa's Village"],
            'correct_answer': 'A'
        },
        {
            'question': "The study of whales, 'Cetology,' is the title of the 32nd chapter of what lengthy American novel?",
            'answers': ['A. The Great Gatsby', 'B. To Kill a Mockingbird', 'C. Moby Dick', 'D. The Catcher in the Rye'],
            'correct_answer': 'C'
        },
        {
            'question': "In 'The Lion, the Witch, and the Wardrobe,' what magical country does the White Witch put a spell on so that it is always winter but never Christmas?",
            'answers': ['A. Middle Earth', 'B. Oz', 'C. Wonderland', 'D. Narnia'],
            'correct_answer': 'D'
        },
        {
            'question': "'Draco Dormiens Nunquam Titillandus,' translated as 'Never Tickle A Sleeping Dragon,' is the official motto for what fictional place of learning?",
            'answers': ['A. Hogwarts', 'B. Brakebills', 'C. Camp Half-Blood', 'D. Starfleet Academy'],
            'correct_answer': 'A'
        },
        {
            'question': "What is this object that was placed under dozens of mattresses in an 1835 literary fairy tale because of its critical role in finding a suitable princess to marry a prince?",
            'answers': ['A. Pearl', 'B. Ruby', 'C. Pea', 'D. Diamond'],
            'correct_answer': 'C'
        },
        {
            'question': "Jack, Simon, Piggy, and Roger are four of the young characters that make up the cast in what 1954 novel?",
            'answers': ['A. 1984', 'B. Animal Farm', 'C. Lord of the Flies', 'D. Brave New World'],
            'correct_answer': 'C'
        }
        ]

    elif category == "Food":
        trivia = [
            {
                'question': "In Greek mythology, what food was considered the food or drink of the Olympian gods?",
                'answers': ['A. Nectar', 'B. Ambrosia', 'C. Honey', 'D. Wine'],
                'correct_answer': 'B'
            },
            {
                'question': "What is the national dish of the United States?",
                'answers': ['A. Hot dog', 'B. Pizza', 'C. Hamburger', 'D. Apple pie'],
                'correct_answer': 'C'
            },
            {
                'question': "Which American city is most famous for its deep-dish pizza?",
                'answers': ['A. New York City', 'B. Los Angeles', 'C. Chicago', 'D. San Francisco'],
                'correct_answer': 'C'
            },
            {
                'question': "What fast-food chain first introduced the drive-thru window?",
                'answers': ['A. McDonald’s', 'B. Burger King', 'C. Wendy’s', 'D. KFC'],
                'correct_answer': 'C'
            },
            {
                'question': "Which fast-food restaurant sells a 'Happy Meal'?",
                'answers': ['A. Wendy’s', 'B. Burger King', 'C. Taco Bell', 'D. McDonald’s'],
                'correct_answer': 'D'
            },
            {
                'question': "Thanksgiving is best known for what three types of food?",
                'answers': ['A. Turkey, mashed potatoes, and green beans', 'B. Ham, sweet potatoes, and pumpkin pie',
                            'C. Turkey, stuffing, and cranberry sauce',
                            'D. Ham, macaroni and cheese, and cornbread'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the name of the rolled raw fish most usually served at Japanese restaurants?",
                'answers': ['A. Sashimi', 'B. Tempura', 'C. Sushi', 'D. Ramen'],
                'correct_answer': 'C'
            },
            {
                'question': "Which country gets credit for developing French fries?",
                'answers': ['A. France', 'B. United States', 'C. Belgium', 'D. United Kingdom'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the most expensive spice in the world when listed by weight?",
                'answers': ['A. Cinnamon', 'B. Vanilla', 'C. Saffron', 'D. Cardamom'],
                'correct_answer': 'C'
            },
            {
                'question': "In what country did brie cheese originate?",
                'answers': ['A. Italy', 'B. Spain', 'C. France', 'D. Switzerland'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the world’s oldest soft drink?",
                'answers': ['A. Coca-Cola', 'B. Pepsi', 'C. Dr. Pepper', 'D. Sprite'],
                'correct_answer': 'C'
            },
            {
                'question': "Which world food is the most popular among all the different continents and countries?",
                'answers': ['A. Sushi', 'B. Tacos', 'C. Pizza and pasta', 'D. Curry'],
                'correct_answer': 'C'
            }
        ]


    elif category == "Geography":
        trivia = [
            {
                'question': "What is the name of the tallest mountain in the world?",
                'answers': ['A. Mount Everest', 'B. K2', 'C. Kangchenjunga', 'D. Lhotse'],
                'correct_answer': 'A'
            },
            {
                'question': "Which country has the largest population in the world?",
                'answers': ['A. India', 'B. United States', 'C. China', 'D. Russia'],
                'correct_answer': 'C'
            },
            {
                'question': "What American city is the Golden Gate Bridge located in?",
                'answers': ['A. Los Angeles', 'B. San Francisco', 'C. New York City', 'D. Chicago'],
                'correct_answer': 'B'
            },
            {
                'question': "What is the capital of Mexico?",
                'answers': ['A. Monterrey', 'B. Cancún', 'C. Guadalajara', 'D. Mexico City'],
                'correct_answer': 'D'
            },
            {
                'question': "What is the name of the largest country in the world?",
                'answers': ['A. Canada', 'B. China', 'C. Russia', 'D. United States'],
                'correct_answer': 'C'
            },
            {
                'question': "Where is the Eiffel Tower located?",
                'answers': ['A. London, England', 'B. Berlin, Germany', 'C. Paris, France', 'D. Rome, Italy'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the capital of Canada?",
                'answers': ['A. Vancouver', 'B. Toronto', 'C. Ottawa', 'D. Montreal'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the name of the largest ocean in the world?",
                'answers': ['A. Atlantic Ocean', 'B. Indian Ocean', 'C. Southern Ocean', 'D. Pacific Ocean'],
                'correct_answer': 'D'
            },
            {
                'question': "What present-day Italian city does Mt. Vesuvius overlook?",
                'answers': ['A. Rome', 'B. Florence', 'C. Milan', 'D. Naples'],
                'correct_answer': 'D'
            },
            {
                'question': "What country are the Great Pyramids of Giza located in?",
                'answers': ['A. Egypt', 'B. Sudan', 'C. Iraq', 'D. Saudi Arabia'],
                'correct_answer': 'A'
            },
            {
                'question': "What is the capital of Thailand?",
                'answers': ['A. Chiang Mai', 'B. Phuket', 'C. Bangkok', 'D. Pattaya'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the name of the smallest country in the world?",
                'answers': ['A. Monaco', 'B. Liechtenstein', 'C. San Marino', 'D. The Vatican City'],
                'correct_answer': 'D'
            },
            {
                'question': "What is the capital of the American State of California?",
                'answers': ['A. Los Angeles', 'B. San Diego', 'C. Sacramento', 'D. San Francisco'],
                'correct_answer': 'C'
            },
            {
                'question': "What country has the most natural lakes?",
                'answers': ['A. Sweden', 'B. Finland', 'C. Canada', 'D. United States'],
                'correct_answer': 'C'
            },
            {
                'question': "How many States does the United States consist of?",
                'answers': ['A. 45', 'B. 48', 'C. 50', 'D. 52'],
                'correct_answer': 'C'
            }
        ]


    elif category == "Movie/TV":
        trivia = [
            {
                'question': "What year did Keeping Up with the Kardashians first premiere?",
                'answers': ['A. 2005', 'B. 2006', 'C. 2007', 'D. 2008'],
                'correct_answer': 'C'
            },
            {
                'question': "Who played Rachel Zane on the legal drama Suits?",
                'answers': ['A. Meghan Markle', 'B. Sarah Rafferty', 'C. Gina Torres', 'D. Abigail Spencer'],
                'correct_answer': 'A'
            },
            {
                'question': "What's the name of the skyscraper in Die Hard?",
                'answers': ['A. Empire State Building', 'B. Nakatomi Plaza', 'C. Willis Tower', 'D. Burj Khalifa'],
                'correct_answer': 'B'
            },
            {
                'question': "What flavor of Pop-Tarts does Buddy the Elf use in his spaghetti in Elf?",
                'answers': ['A. Strawberry', 'B. Chocolate', 'C. Blueberry', 'D. Cinnamon'],
                'correct_answer': 'B'
            },
            {
                'question': "What pop vocal group performs at the wedding in Bridesmaids?",
                'answers': ['A. Destiny\'s Child', 'B. Wilson Phillips', 'C. Spice Girls', 'D. Backstreet Boys'],
                'correct_answer': 'B'
            },
            {
                'question': "The head of what kind of animal is front and center in an infamous scene from The Godfather?",
                'answers': ['A. Cow', 'B. Horse', 'C. Cat', 'D. Dog'],
                'correct_answer': 'B'
            },
            {
                'question': "For which 1964 musical blockbuster did Julie Andrews win the Academy Award for Best Actress?",
                'answers': ['A. West Side Story', 'B. The Sound of Music', 'C. Mary Poppins', 'D. My Fair Lady'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the highest-grossing R-rated movie of all time?",
                'answers': ['A. Deadpool', 'B. The Matrix', 'C. Joker', 'D. The Hangover'],
                'correct_answer': 'C'
            },
            {
                'question': "What year was the movie Gone With The Wind released?",
                'answers': ['A. 1937', 'B. 1938', 'C. 1939', 'D. 1940'],
                'correct_answer': 'C'
            },
            {
                'question': "What A24 film was released in 2022 and won Best Picture at the Academy Awards?",
                'answers': ['A. The Florida Project', 'B. Moonlight', 'C. Lady Bird', 'D. Everything Everywhere All At Once'],
                'correct_answer': 'D'
            },
            {
                'question': "Who directed the 2017 film Get Out?",
                'answers': ['A. Jordan Peele', 'B. Spike Lee', 'C. Ava DuVernay', 'D. Ryan Coogler'],
                'correct_answer': 'A'
            },
            {
                'question': "What is the name of the fictional African country in the movie Black Panther?",
                'answers': ['A. Zamunda', 'B. Wakanda', 'C. Genovia', 'D. Sokovia'],
                'correct_answer': 'B'
            },
            {
                'question': "What gift does Rose find in her coat pocket at the end of Titanic?",
                'answers': ['A. A diamond ring', 'B. A love letter', 'C. A necklace', 'D. A ticket'],
                'correct_answer': 'C'
            },
            {
                'question': "What score does Elle get on her LSAT exam in Legally Blonde?",
                'answers': ['A. 160', 'B. 170', 'C. 179', 'D. 180'],
                'correct_answer': 'C'
            },
            {
                'question': "Who is the director of Oppenheimer?",
                'answers': ['A. Steven Spielberg', 'B. Christopher Nolan', 'C. Quentin Tarantino', 'D. Martin Scorsese'],
                'correct_answer': 'B'
            },
            {
                'question': "What breakfast food does Donkey want to make with Shrek in Shrek?",
                'answers': ['A. Pancakes', 'B. Waffles', 'C. Bacon and eggs', 'D. Cereal'],
                'correct_answer': 'B'
            },
            {
                'question': "In Willy Wonka & the Chocolate Factory, who is the first kid the Oompa Loompas sing about?",
                'answers': ['A. Augustus Gloop', 'B. Veruca Salt', 'C. Violet Beauregarde', 'D. Mike Teavee'],
                'correct_answer': 'A'
            }
        ]


    elif category == "Sports":
        trivia = [
            {
                'question': "Home of Major League Baseball’s Toronto Blue Jays, the Rogers Centre opened in 1989 as the SkyDome – the world’s first sports arena to feature a fully retractable what?",
                'answers': ['A. Roof', 'B. Field', 'C. Grandstand', 'D. Scoreboard'],
                'correct_answer': 'A'
            },
            {
                'question': "What is the feline name of the sports teams of Northwestern University?",
                'answers': ['A. Cougars', 'B. Tigers', 'C. Wildcats', 'D. Panthers'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the name of the 2020 ESPN sports documentary miniseries that focused on Michael Jordan's final season with the Chicago Bulls?",
                'answers': ['A. The Last Dance', 'B. Air Jordan', 'C. Bulls Run', 'D. Slam Dunk'],
                'correct_answer': 'A'
            },
            {
                'question': "Steve Yzerman is a Detroit sports icon in which sport?",
                'answers': ['A. Basketball', 'B. Baseball', 'C. Football', 'D. Hockey'],
                'correct_answer': 'D'
            },
            {
                'question': "What sport did Honus Wagner famously play?",
                'answers': ['A. Football', 'B. Baseball', 'C. Basketball', 'D. Soccer'],
                'correct_answer': 'B'
            },
            {
                'question': "What six-letter word names both a seed company and an exercise that combines a squat, a pushup, and a jump in the air?",
                'answers': ['A. Burpee', 'B. Crunch', 'C. Sprint', 'D. Plank'],
                'correct_answer': 'A'
            },
            {
                'question': "What sport has defensive positions named gully, silly mid-off, and deep mid wicket?",
                'answers': ['A. Cricket', 'B. Soccer', 'C. Rugby', 'D. Field Hockey'],
                'correct_answer': 'A'
            },
            {
                'question': "Outside what sports venue would you find “Rise Up,” the world’s largest freestanding sculpture of a bird?",
                'answers': ['A. Staples Center', 'B. Wembley Stadium', 'C. Mercedes-Benz Stadium',
                            'D. Madison Square Garden'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the name of the pipeline, built in the 1970s, that transports oil from fields near Prudhoe Bay across Alaska to the port city of Valdez?",
                'answers': ['A. Keystone Pipeline', 'B. Trans-Alaska Pipeline', 'C. Alaskan Pipeline',
                            'D. Arctic Pipeline'],
                'correct_answer': 'B'
            },
            {
                'question': "\"The Run for the Roses\" and \"The Fastest Two Minutes in Sports\" are both colloquial names for a horse race that occurs on the first Saturday of May in which U.S. State?",
                'answers': ['A. Kentucky', 'B. California', 'C. Texas', 'D. New York'],
                'correct_answer': 'A'
            },
            {
                'question': "A large brown bear named Blades is the mascot of what Boston professional sports team?",
                'answers': ['A. New England Patriots', 'B. Boston Red Sox', 'C. Boston Celtics', 'D. Boston Bruins'],
                'correct_answer': 'D'
            },
            {
                'question': "The Musketeers, who play in the NCAA's Big East Conference, are the sports teams of what private university located in Cincinnati?",
                'answers': ['A. University of Cincinnati', 'B. Ohio State University', 'C. Xavier University',
                            'D. Miami University'],
                'correct_answer': 'C'
            },
            {
                'question': "The Dukes are the Division I sports teams of what educational institution located in the Uptown neighborhood of Pittsburgh?",
                'answers': ['A. University of Pittsburgh', 'B. Carnegie Mellon University', 'C. Duquesne University',
                            'D. Point Park University'],
                'correct_answer': 'C'
            },
            {
                'question': "\"Pistol Pete\" Maravich (1970) and Shaquille O'Neal both won player of the year honors while playing hoops for what university?",
                'answers': ['A. University of Florida', 'B. Duke University', 'C. Louisiana State University',
                            'D. University of Kentucky'],
                'correct_answer': 'C'
            },
            {
                'question': "The Tartans, who play in NCAA Division III, are the sports teams of what Pittsburgh university?",
                'answers': ['A. University of Pittsburgh', 'B. Carnegie Mellon University', 'C. Duquesne University',
                            'D. Point Park University'],
                'correct_answer': 'B'
            },
            {
                'question': "Which legendary left-handed American sportsman had the little-used first names \"George Hermann\"?",
                'answers': ['A. Babe Ruth', 'B. Muhammad Ali', 'C. Michael Jordan', 'D. Tiger Woods'],
                'correct_answer': 'A'
            },
            {
                'question': "What’s the name of the French brand of luxury sports cars that includes the Veyron, Chiron, and Divo?",
                'answers': ['A. Ferrari', 'B. Lamborghini', 'C. Bugatti', 'D. Porsche'],
                'correct_answer': 'C'
            },
            {
                'question': "In 1960, which president wrote an article for 'Sports Illustrated' (entitled 'The Soft American') and created fitness councils to come up with physical education curriculums for schools?",
                'answers': ['A. Dwight D. Eisenhower', 'B. John F. Kennedy', 'C. Lyndon B. Johnson',
                            'D. Richard Nixon'],
                'correct_answer': 'B'
            },
            {
                'question': "Stamford, Connecticut is the home of what media and entertainment company known for “Sports Entertainment”, as Vince McMahon likes to call his performance product?",
                'answers': ['A. ESPN', 'B. Fox Sports', 'C. WWE', 'D. NBC Sports'],
                'correct_answer': 'C'
            },
            {
                'question': "Mount Whitney is the finish line for a race that starts 135 miles earlier at Badwater, the scorching basin of what national park?",
                'answers': ['A. Grand Canyon National Park', 'B. Yellowstone National Park',
                            'C. Yosemite National Park', 'D. Death Valley National Park'],
                'correct_answer': 'D'
            },
            {
                'question': "The Washington Capitals defeated what team in the 2018 Stanley Cup Finals?",
                'answers': ['A. Pittsburgh Penguins', 'B. Nashville Predators', 'C. Vegas Golden Knights',
                            'D. Tampa Bay Lightning'],
                'correct_answer': 'C'
            },
            {
                'question': "What North Carolina sports team plays its home games at PNC Arena in Raleigh and has a mascot called Stormy?",
                'answers': ['A. Carolina Panthers', 'B. Charlotte Hornets', 'C. Carolina Hurricanes',
                            'D. Duke Blue Devils'],
                'correct_answer': 'C'
            }
        ]

    elif category == "Howard":
        trivia = [
            {
                'question': "Who founded Howard?",
                'answers': ['A. Martin Luther King Jr.', 'B. First Congregational Society of Washington', 'C. NAACP', 'D. Booker T. Washington'],
                'correct_answer': 'B'
            },
            {
                'question': "How many people founded Howard?",
                'answers': ['A. 5', 'B. 10', 'C. 15', 'D. 20'],
                'correct_answer': 'B'
            },
            {
                'question': "Who was the university named for?",
                'answers': ['A. Howard Hughes', 'B. General Oliver Otis Howard', 'C. John Howard', 'D. Howard Stark'],
                'correct_answer': 'B'
            },
            {
                'question': "What year was Howard University founded?",
                'answers': ['A. 1855', 'B. 1860', 'C. 1865', 'D. 1867'],
                'correct_answer': 'D'
            },
            {
                'question': "How much was tuition in 1865?",
                'answers': ['A. 50 cents per month', 'B. 75 cents per month', 'C. 1 dollar per month',
                            'D. 1.25 dollars per month'],
                'correct_answer': 'C'
            },
            {
                'question': "How much was room and board in 1867?",
                'answers': ['A. 1 dollar per term', 'B. 2 dollars per term', 'C. 3 dollars per term',
                            'D. 4 dollars per term'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the only remaining original building and where is it listed?",
                'answers': ['A. Founders Hall, National Register of Historic Places',
                            'B. Howard Hall, National Register of Historic Places',
                            'C. Main Administration Building, National Historic Landmark',
                            'D. The Quad, National Historic Site'],
                'correct_answer': 'B'
            },
            {
                'question': "How many acres is the university and how many campuses?",
                'answers': ['A. 100 acres, one campus', 'B. 200 acres, two campuses', 'C. 241 acres, three campuses',
                            'D. 300 acres, four campuses'],
                'correct_answer': 'C'
            },
            {
                'question': "Who was the university's first black president?",
                'answers': ['A. Mordecai W. Johnson', 'B. Frederick Douglass', 'C. Booker T. Washington',
                            'D. W.E.B. Du Bois'],
                'correct_answer': 'A'
            },
            {
                'question': "What are the black greek fraternities and sororities?",
                'answers': ['A. Delta Sigma Theta, Alpha Phi Alpha, Omega Psi Phi',
                            'B. Alpha Kappa Alpha, Alpha Phi Alpha, Zeta Phi Beta',
                            'C. Phi Beta Sigma, Delta Sigma Theta, Omega Psi Phi',
                            'D. Alpha Kappa Alpha, Alpha Phi Alpha, Delta Sigma Theta'],
                'correct_answer': 'B'
            },
            {
                'question': "What was the first fraternity founded at Howard?",
                'answers': ['A. Omega Psi Phi', 'B. Alpha Phi Alpha', 'C. Kappa Alpha Psi', 'D. Phi Beta Sigma'],
                'correct_answer': 'B'
            },
            {
                'question': "What was the first predominantly African American fraternity founded at a HBCU?",
                'answers': ['A. Omega Psi Phi', 'B. Alpha Phi Alpha', 'C. Kappa Alpha Psi', 'D. Phi Beta Sigma'],
                'correct_answer': 'A'
            },
            {
                'question': "Who was the first Howard alumnus elected Head of the University and when?",
                'answers': ['A. Dr. Franklin G. Jenifer - December 16, 1969',
                            'B. Dr. Mordecai W. Johnson - January 1, 1926',
                            'C. Dr. Wayne A. I. Frederick - February 1, 2014', 'D. Dr. James E. Cheek - May 1, 1969'],
                'correct_answer': 'A'
            },
            {
                'question': "Who coined the phrase for 'leadership in America and the global community'?",
                'answers': ['A. Dr. Mordecai W. Johnson', 'B. Dr. Wayne A. I. Frederick', 'C. H. Patrick Swygert',
                            'D. Dr. Franklin G. Jenifer'],
                'correct_answer': 'C'
            },
            {
                'question': "Who is the current president?",
                'answers': ['A. Dr. Franklin G. Jenifer', 'B. Dr. Wayne A. I. Frederick', 'C. Dr. Mordecai W. Johnson',
                            'D. H. Patrick Swygert'],
                'correct_answer': 'B'
            },
            {
                'question': "How many campuses are there today?",
                'answers': ['A. 1', 'B. 2', 'C. 3', 'D. 4'],
                'correct_answer': 'D'
            },
            {
                'question': "Approximately how many students are enrolled today?",
                'answers': ['A. 5,000', 'B. 7,500', 'C. 10,000', 'D. 11,000'],
                'correct_answer': 'D'
            },
            {
                'question': "How many schools and colleges are there today?",
                'answers': ['A. 6', 'B. 8', 'C. 10', 'D. 12'],
                'correct_answer': 'D'
            },
            {
                'question': "How many faculty are there today?",
                'answers': ['A. more than 800', 'B. more than 1,000', 'C. more than 1,200', 'D. more than 1,400'],
                'correct_answer': 'D'
            },
            {
                'question': "How many areas of study are there today and what are they?",
                'answers': ['A. 80 undergrad, 90 grad, 20 doctorate', 'B. 90 undergrad, 100 grad, 30 doctorate',
                            'C. 100 undergrad, 110 grad, 40 doctorate', 'D. 80 undergrad, 91 grad, 21 doctorate'],
                'correct_answer': 'D'
            },
            {
                'question': "What was the original motto?",
                'answers': ['A. Truth and Service', 'B. For God and Truth', 'C. Equal Rights and Knowledge for All',
                            'D. Freedom and Justice'],
                'correct_answer': 'C'
            },
            {
                'question': "Who are some notable alumni?",
                'answers': ['A. Rosa Parks, Martin Luther King Jr., Maya Angelou',
                            'B. Thurgood Marshall, Debbie Allen, Toni Morrison',
                            'C. Malcolm X, W.E.B. Du Bois, Angela Davis',
                            'D. Phyllicia Rashad, Jesse Jackson, Barack Obama'],
                'correct_answer': 'B'
            }
        ]


    elif category == "Animal":
        trivia = [
            {
                'question': "What is the largest known land animal?",
                'answers': ['A. Giraffe', 'B. Elephant', 'C. Hippopotamus', 'D. Rhinoceros'],
                'correct_answer': 'B'
            },
            {
                'question': "Animals that eat both plants and meat are called what?",
                'answers': ['A. Herbivores', 'B. Carnivores', 'C. Omnivores', 'D. Vegetarians'],
                'correct_answer': 'C'
            },
            {
                'question': "How many bones do sharks have?",
                'answers': ['A. 0', 'B. 206', 'C. 300', 'D. 412'],
                'correct_answer': 'A'
            },
            {
                'question': "The dingo is a free-ranging dog found mainly in which country?",
                'answers': ['A. United States', 'B. Canada', 'C. Australia', 'D. Russia'],
                'correct_answer': 'C'
            },
            {
                'question': "On what continent would you not find bees?",
                'answers': ['A. North America', 'B. Europe', 'C. Asia', 'D. Antarctica'],
                'correct_answer': 'D'
            },
            {
                'question': "Which animal has the largest brain?",
                'answers': ['A. Elephant', 'B. Blue Whale', 'C. Human', 'D. Sperm Whale'],
                'correct_answer': 'D'
            },
            {
                'question': "What is a baby swan called?",
                'answers': ['A. Chick', 'B. Gosling', 'C. Cygnet', 'D. Duckling'],
                'correct_answer': 'C'
            },
            {
                'question': "What is a group of lions called?",
                'answers': ['A. Pack', 'B. Flock', 'C. Herd', 'D. Pride'],
                'correct_answer': 'D'
            },
            {
                'question': "Which snake, whose untreated bite is almost 100 percent fatal, is the world’s fastest snake on land?",
                'answers': ['A. Black Mamba', 'B. King Cobra', 'C. Rattlesnake', 'D. Coral Snake'],
                'correct_answer': 'A'
            },
            {
                'question': "What is the only mammal born with horns?",
                'answers': ['A. Rhino', 'B. Elephant', 'C. Giraffe', 'D. Buffalo'],
                'correct_answer': 'C'
            },
            {
                'question': "Which marine animal is the only known natural predator of the great white shark?",
                'answers': ['A. Killer Whale', 'B. Great White Shark', 'C. Tiger Shark', 'D. Hammerhead Shark'],
                'correct_answer': 'A'
            }
        ]

    elif category == "Disney":
        trivia = [
            {
                'question': 'What is the first “themed land” just inside the main entrance of Disneyland?',
                'answers': ['A. Adventureland', 'B. Fantasyland', 'C. Frontierland', 'D. Main Street, U.S.A.'],
                'correct_answer': 'D'
            },
            {
                'question': 'What was Walt Disney’s middle name?',
                'answers': ['A. Roy', 'B. Frank', 'C. Elias', 'D. Jacob'],
                'correct_answer': 'C'
            },
            {
                'question': 'Which is the name of one of the 7 dwarfs from the Disney movie “Snow White and the Seven Dwarfs”?',
                'answers': ['A. Sneezy', 'B. Sporty', 'C. Silly', 'D. Smelly'],
                'correct_answer': 'A'
            },
            {
                'question': 'In the movie “The Lion King”, what was Simba’s mother’s name?',
                'answers': ['A. Nala', 'B. Sarafina', 'C. Sarabi', 'D. Shenzi'],
                'correct_answer': 'C'
            },
            {
                'question': 'In which US city was Walt Disney born?',
                'answers': ['A. Los Angeles, California', 'B. San Francisco, California', 'C. Chicago, Illinois',
                            'D. New York City, New York'],
                'correct_answer': 'C'
            },
            {
                'question': 'What was the name of the kleptomaniac monkey in the Disney movie “Aladdin”?',
                'answers': ['A. Rajah', 'B. Abu', 'C. Iago', 'D. Zazu'],
                'correct_answer': 'B'
            },
            {
                'question': 'In Disney’s “The Little Mermaid” what is the name of the human that Ariel falls in love with?',
                'answers': ['A. Prince Charming', 'B. Prince Eric', 'C. Prince Philip', 'D. Prince Adam'],
                'correct_answer': 'B'
            },
            {
                'question': "Released in 1941, what is the only Disney animated feature film with a title character that never speaks?",
                'answers': ['A. Bambi', 'B. Pinocchio', 'C. Dumbo', 'D. Snow White and the Seven Dwarfs'],
                'correct_answer': 'C'
            },
            {
                'question': "What food is Tiana famous for in The Princess and The Frog?",
                'answers': ['A. Beignets', 'B. Croissants', 'C. Macarons', 'D. Cupcakes'],
                'correct_answer': 'A'
            },
            {
                'question': "How many fingers does Mickey Mouse have?",
                'answers': ['A. Three', 'B. Four', 'C. Five', 'D. Six'],
                'correct_answer': 'B'
            },
            {
                'question': "How old is Meredith Blake in 1998's The Parent Trap?",
                'answers': ['A. 24', 'B. 26', 'C. 28', 'D. 30'],
                'correct_answer': 'B'
            },
            {
                'question': "What is the name of Goofy's son?",
                'answers': ['A. Pluto', 'B. Max', 'C. Donald', 'D. Huey'],
                'correct_answer': 'B'
            },
            {
                'question': "What was the first Pixar movie?",
                'answers': ['A. Finding Nemo', 'B. Toy Story', 'C. Monsters, Inc.', 'D. The Incredibles'],
                'correct_answer': 'B'
            },
            {
                'question': "What does Mulan call herself when pretending to be a man?",
                'answers': ['A. Yao', 'B. Ling', 'C. Ping', 'D. Shang'],
                'correct_answer': 'C'
            },
            {
                'question': "What are the names of the fox and the hound from The Fox and the Hound?",
                'answers': ['A. Copper and Todd', 'B. Max and Duke', 'C. Tod and Copper', 'D. Skipper and Oliver'],
                'correct_answer': 'C'
            },
            {
                'question': "Which Disney movie features a character named Baymax?",
                'answers': ['A. Frozen', 'B. Big Hero 6', 'C. Moana', 'D. Zootopia'],
                'correct_answer': 'B'
            },
            {
                'question': "What is the name of the demigod who accompanies Moana on her journey in Moana?",
                'answers': ['A. Maui', 'B. Heihei', 'C. Te Fiti', 'D. Tamatoa'],
                'correct_answer': 'A'
            },
            {
                'question': "What is the name of the teapot character in Beauty and the Beast?",
                'answers': ['A. Mrs. Potts', 'B. Chip', 'C. Lumière', 'D. Cogsworth'],
                'correct_answer': 'A'
            },
            {
                'question': "In Beauty and the Beast, what enchanted household object is Lumiere?",
                'answers': ['A. Teapot', 'B. Clock', 'C. Candlestick', 'D. Wardrobe'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the name of Elsa and Anna's kingdom in Frozen?",
                'answers': ['A. Corona', 'B. Arendelle', 'C. Camelot', 'D. Avalon'],
                'correct_answer': 'B'
            },
            {
                'question': "Which Disney princess has a raccoon as a sidekick?",
                'answers': ['A. Cinderella', 'B. Ariel', 'C. Pocahontas', 'D. Belle'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the name of Simba's father in The Lion King?",
                'answers': ['A. Scar', 'B. Rafiki', 'C. Timon', 'D. Mufasa'],
                'correct_answer': 'D'
            },
            {
                'question': "What is the name of the toy store in Toy Story 2?",
                'answers': ['A. Andy’s Toy Barn', 'B. Sid’s Toy Emporium', 'C. Al’s Toy Barn', 'D. Woody’s Toy Market'],
                'correct_answer': 'C'
            },
            {
                'question': "Where does Mike Wazowski take his girlfriend Celia for her birthday dinner in Monster's, Inc.?",
                'answers': ['A. Harryhausen’s', "B. Tony's Italian Restaurant", 'C.Chez Gusteau', 'D.Chez Remy'],
                                                                                                              'correct_answer': 'A'
            },
            {
                'question': "Who does Tiana fall in love with in The Princess and the Frog?",
                'answers': ['A. Prince Eric', 'B. Prince Adam', 'C. Prince Naveen', 'D. Prince Charming'],
                'correct_answer': 'C'
            },
            {
                'question': "In Finding Nemo, what's the name of Nemo's mother?",
                'answers': ['A. Coral', 'B. Dory', 'C. Marlin', 'D. Pearl'],
                'correct_answer': 'A'
            },
            {
                'question': "What were the first words Mickey Mouse ever spoke?",
                'answers': ['A. Oh boy!', 'B. Hiya, folks!', 'C. Hot dog!', 'D. Golly!'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the name of Ariel and Eric's daughter in The Little Mermaid II: Return to the Sea?",
                'answers': ['A. Ariel Jr.', 'B. Melody', 'C. Harmony', 'D. Coral'],
                'correct_answer': 'B'
            },
            {
                'question': "How many ghosts live in the Haunted Mansion?",
                'answers': ['A. 666', 'B. 777', 'C. 888', 'D. 999'],
                'correct_answer': 'D'
            },
            {
                'question': "What type of bug is the main character in A Bug's Life?",
                'answers': ['A. Beetle', 'B. Butterfly', 'C. Ant', 'D. Grasshopper'],
                'correct_answer': 'C'
            },
            {
                'question': "What famous actor voiced Lightning McQueen in Cars?",
                'answers': ['A. Tom Hanks', 'B. Owen Wilson', 'C. Will Smith', 'D. Johnny Depp'],
                'correct_answer': 'B'
            },
            {
                'question': "Where does Enchanted take place?",
                'answers': ['A. Los Angeles', 'B. Chicago', 'C. New York City', 'D. Miami'],
                'correct_answer': 'C'
            },
            {
                'question': "Who composed the music for The Lion King?",
                'answers': ['A. Hans Zimmer', 'B. Elton John', 'C. Alan Menken', 'D. Randy Newman'],
                'correct_answer': 'B'
            },
            {
                'question': "Who voices the character of Elsa in Frozen?",
                'answers': ['A. Kristen Bell', 'B. Idina Menzel', 'C. Jennifer Lee', 'D. Demi Lovato'],
                'correct_answer': 'B'
            },
            {
                'question': "Which Disney animated film was the first to receive an Academy Award nomination for Best Picture?",
                'answers': ['A. Beauty and the Beast (1991)', 'B. The Lion King', 'C. Aladdin',
                            'D. Snow White and the Seven Dwarfs'],
                'correct_answer': 'A'
            },
            {
                'question': "In what year did Mickey Mouse make his first appearance?",
                'answers': ['A. 1925', 'B. 1928', 'C. 1933', 'D. 1938'],
                'correct_answer': 'B'
            },
            {
                'question': "Who is the composer of the music for The Nightmare Before Christmas?",
                'answers': ['A. Danny Elfman', 'B. Alan Menken', 'C. Randy Newman', 'D. Hans Zimmer'],
                'correct_answer': 'A'
            },
            {
                'question': "What is the name of the chef in Ratatouille who aspires to be a great chef despite being a rat?",
                'answers': ['A. Gusteau', 'B. Linguini', 'C. Emile', 'D. Remy'],
                'correct_answer': 'D'
            },
            {
                'question': "What is the name of Pocahontas's pet raccoon?",
                'answers': ['A. Meeko', 'B. Flit', 'C. Percy', 'D. Kocoum'],
                'correct_answer': 'A'
            },
            {
                'question': "Who is the main character in The Hunchback of Notre Dame?",
                'answers': ['A. Phoebus', 'B. Frollo', 'C. Esmeralda', 'D. Quasimodo'],
                'correct_answer': 'D'
            },
            {
                'question': "Who is the villain in The Little Mermaid?",
                'answers': ['A. Ursula', 'B. Maleficent', 'C. Cruella de Vil', 'D. Jafar'],
                'correct_answer': 'A'
            },
            {
                'question': "In Up, which continent do Carl and Russell travel to?",
                'answers': ['A. Asia', 'B. Africa', 'C. Europe', 'D. South America'],
                'correct_answer': 'D'
            }
        ]

    elif category == "Science":
        trivia = [
            {
                'question': "Diabetes develops as the result of a problem with which specific organ in the body?",
                'answers': ['A. Liver', 'B. Kidney', 'C. Pancreas', 'D. Heart'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the rarest blood type?",
                'answers': ['A. O+', 'B. AB+', 'C. A-', 'D. AB-'],
                'correct_answer': 'D'
            },
            {
                'question': "What is it called when you make light change direction by passing it through a lens?",
                'answers': ['A. Reflection', 'B. Absorption', 'C. Diffraction', 'D. Refraction'],
                'correct_answer': 'D'
            },
            {
                'question': "In what month does winter begin in the Southern Hemisphere?",
                'answers': ['A. December', 'B. June', 'C. September', 'D. November'],
                'correct_answer': 'B'
            },
            {
                'question': "Which is the most abundant element in the universe?",
                'answers': ['A. Oxygen', 'B. Carbon', 'C. Helium', 'D. Hydrogen'],
                'correct_answer': 'D'
            },
            {
                'question': "How many colors are in the rainbow?",
                'answers': ['A. Five', 'B. Six', 'C. Seven', 'D. Eight'],
                'correct_answer': 'C'
            },
            {
                'question': "The concept of gravity was discovered by which famous physicist?",
                'answers': ['A. Albert Einstein', 'B. Nikola Tesla', 'C. Galileo Galilei', 'D. Sir Isaac Newton'],
                'correct_answer': 'D'
            },
            {
                'question': "What is the hardest natural substance on Earth?",
                'answers': ['A. Quartz', 'B. Graphene', 'C. Diamond', 'D. Corundum'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the nearest planet to the sun?",
                'answers': ['A. Venus', 'B. Earth', 'C. Mars', 'D. Mercury'],
                'correct_answer': 'D'
            },
            {
                'question': "How many elements are there in the periodic table?",
                'answers': ['A. 92', 'B. 103', 'C. 118', 'D. 120'],
                'correct_answer': 'C'
            },
            {
                'question': "What is the quality of an object that allows it to float on water?",
                'answers': ['A. Density', 'B. Weight', 'C. Volume', 'D. Buoyancy'],
                'correct_answer': 'D'
            },
            {
                'question': "What is the largest internal organ of the human body?",
                'answers': ['A. Heart', 'B. Brain', 'C. Kidney', 'D. Liver'],
                'correct_answer': 'D'
            },
            {
                'question': "What type of bond involves the sharing of electron pairs between different atoms?",
                'answers': ['A. Ionic', 'B. Metallic', 'C. Covalent', 'D. Hydrogen'],
                'correct_answer': 'C'
            },
            {
                'question': "Oncology focuses on what disease?",
                'answers': ['A. Diabetes', 'B. Cardiovascular disease', 'C. Alzheimer\'s disease', 'D. Cancer'],
                'correct_answer': 'D'
            },
            {
                'question': "What planet in our solar system has the most gravity?",
                'answers': ['A. Earth', 'B. Mars', 'C. Saturn', 'D. Jupiter'],
                'correct_answer': 'D'
            },
            {
                'question': "Penicillin is used to fight what type of infections?",
                'answers': ['A. Viral', 'B. Fungal', 'C. Parasitic', 'D. Bacterial'],
                'correct_answer': 'D'
            },
            {
                'question': "What is the medical term for bad breath?",
                'answers': ['A. Dyspepsia', 'B. Dysphagia', 'C. Halitosis', 'D. Gingivitis'],
                'correct_answer': 'C'
            },
            {
                'question': "The study of the weather is called what?",
                'answers': ['A. Geology', 'B. Climatology', 'C. Meteorology', 'D. Seismology'],
                'correct_answer': 'C'
            }
        ]

    return random.choice(trivia)






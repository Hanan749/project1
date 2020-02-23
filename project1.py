"""
Homework #2 : Word Histogram
Hannan Ikhlayel
"""

input_text1= """
The devil is not in the details of the "deal of the century". The map that United States President Donald Trump
tweeted on January 28 following the announcement of his Middle East plan shows what looks like a slice of Swiss
cheese rather than of a sovereign Palestinian state.But for Trump's main supporters - people like gambling tycoon
Sheldon Adelson and his wife, Miriam Adelson, who stood in the front row during the announcement ceremony in the
White House - this was yet another win.These days, it is people like Adelson, rich conservative donors to the Trump
campaign, along with the president's evangelical base, who are calling the shots in Washington and Jerusalem. They 
are always there, in the front row. They appeared satisfied and beaming at the 2018 inauguration of the US Embassy
in Jerusalem - a move they had badgered and cajoled the president to make. He obviously did not regret it, even 
though the Palestinians severed ties with Washington as a result.As far as Adelson is concerned, "the Palestinians
are an invented people" whose sole purpose on Earth is to destroy Israel. Adelson was also among those who 
encouraged Trump to pull the US out of the nuclear agreement with Iran. He thinks Iran should have been nuked.
The corrupt symbiosis of money, power and media is no secret. In a June 2019 opinion piece in the freebie Israel
Hayom newspaper, the Adelsons' biggest endowment to Israel's political right, Miriam Adelson gushed, "Trump should 
enjoy sweeping support among US Jews, just as he does among Israelis. That this has not been the case 
(so far; the 2020 election still beckons) is an oddity that will long be pondered by historians. Scholars of the
Bible will no doubt note the heroes, sages, and prophets of antiquity who were similarly spurned by the very people
they came to raise up. Would it be too much to pray for a day when the Bible gets a 'Book of Trump'?"
She ended her article suggesting, "Until that is decided, let us, at least, sit back and marvel at this time of
miraclesfor Israel, for the United States, and for the whole world". No less.But Israeli Prime Minister Benjamin
Netanyahu will find it hard "to sit back and marvel". He will need a real miracle to extricate himself from 
criminal conviction. All of Adelson's billions cannot stop the wheels of justice spinning in Jerusalem.
While Netanyahu was waxing poetic in Washington about a "historic moment", history was being made in Jerusalem
with the first-ever court filing of a criminal indictment against an incumbent Israeli prime minister. Unlike 
Trump, whose Senate-majority support is expected to save him from removal after the impeachment, Netanyahu has
lost his majority in the Israeli legislature.
""".lower()
input_text2= """
The host, US President Donald Trump, and the guest of honour, Israel's Prime Minister Benjamin Netanyahu, 
backslappingly beamed at each other. The guests drawn from the entourages of the two leaders clapped and whooped.
The biggest cheers were for President Trump's reminders of what he has done for Israel. Prime Minister Netanyahu 
said the day would be remembered in the same breath as Israel's day of independence in 1948. It was, said Mr
Netanyahu, one of the most important moments of his life.President Trump says he has found a new way to make peace
between Israel and the Palestinians. Israel will get the security it needs. Palestinians will get the state they
crave.So far so good - except that the Trump plan gives Mr Netanyahu all he wants - and offers Palestinians very
little; a sort-of state that will be truncated, without proper sovereignty, surrounded by Israel's territory and
threaded between Jewish settlements.Peace seemed possible, oncePresident Trump may believe, truly and without 
doubt, that he is offering the "deal of the century". It is a great deal for Mr Netanyahu and his government.
Their positions on the Palestinians, more than ever, are America's positions.Smiles and sorrow on the ground
Can the Jewish settlement issue be resolved?Are there alternatives to a two-state solution?What makes Jerusalem
so holy?Through all the years of mediation in peace talks between Israel and the Palestinians, the top US 
priorities have always been Israel's wishes, constraints and most of all its security. But successive US presidents
accepted that peace required a viable Palestinian state alongside Israel, even if they were not prepared to allow it equal sovereignty.
Israel argues the Palestinians turned down a series of good offers. The Palestinian negotiators say they made 
huge concessions, not least accepting Israel's existence in around 78% of their historic homeland.
""".lower()

print(input_text1)
print(input_text2)

irrelevent_words = {". ", ", ", " and ", " or ", " the ", " among ", " people ", " y ", " with ", " he ", "the",
                    " like ", " a ", " to ", " is ", " of ", " for "
    , " is ", " was ", " so ", " it ", " its ", " not ", " in ", " at ", " be ", " his ", " that ", " her ", " who "
    , " no ", " on ", " an ", " are ", " there ", " as ", " will ", "-", " has ", " they ", " this ", " so ", " us ",
                    " all ", " between "}
for iw in irrelevent_words:
    input_text1 = input_text1.replace(iw, " ")
    input_text2 = input_text2.replace(iw, " ")

print(input_text1)
print(input_text2)

word_list1 = input_text1.split()
word_list2 = input_text2.split()

print(word_list1)
print(word_list2)

word_histogram1 = {}
word_histogram2 = {}

for word1 in word_list1:
    if word1 not in word_histogram1.keys():
        word_histogram1[word1] = 1
    else:
        word_histogram1[word1] = word_histogram1[word1] + 1

for word2 in word_list2:
    if word2 not in word_histogram2.keys():
        word_histogram2[word2] = 1
    else:
        word_histogram2[word2] = word_histogram2[word2] + 1

print(word_histogram1)
print(word_histogram2)

sorted_d1 = sorted(word_histogram1.items(), key=operator.itemgetter(1))
print(sorted_d1)

sorted_d2 = sorted(word_histogram2.items(), key=operator.itemgetter(1))
print(sorted_d2)

sorted_file1 = sorted_d1[-6:]
sorted_file2 = sorted_d2[-6:]
print(sorted_file1)
print(sorted_file2)

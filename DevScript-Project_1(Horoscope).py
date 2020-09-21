# Program to print the Horoscope of the User.
while True:
	Forecast=False
	Choice=int(input('''
1) Aries Horoscope
2) Taurus Horoscope
3) Gemini Horoscope
4) Cancer Horoscope
5) Leo Horoscope
6) Virgo Horoscope
7) Libra Horoscope
8) Scorpio Horoscope
9) Sagittarius Horoscope
10) Capricorn Horoscope
11) Aquarius Horoscope
12) Pisces Horoscope
\nPress any no. from a given List to forecast your Horoscope:'''))

	if Choice==1:
		Forecast='''
Aries Horoscope:

What's been done cannot be undone, Aries. But do you really want to carry the burden of your past into the future? Something to think about in the days to come. The Universe is giving you the chance to cleanse and purge, to let go of your excess baggage, and heal the relationships that stand on shaky ground. Ho'oponopono is a wonderful Hawaiian prayer that will alleviate the process of forgiveness. "I am sorry. Please forgive me. Thank you. I love you." Consider repeating these words a few times everyday with the person or situation in your mind, or write it down on paper.

Cosmic tip: It's time to make peace with your past.
'''

	elif Choice==2:
		Forecast='''
Taurus Horoscope:

Taurus, visualise a parallel reality for yourself, where everything is working out seamlessly. The help and support you need is available to you at each step. The abundance you desire is constantly flowing in as well. Now visualise a door that leads to this portal and allow yourself to step in. Program every fibre of your being to believe that you deserve to live a life of greatness, and allow yourself to receive the blessings. Overheard at the cosmic conference: you are ready to rewrite the script.

Cosmic tip: Ready to rewrite the script of your life?
'''

	elif Choice==3:
		Forecast='''
Gemini Horoscope:

Gemini, you are a master manifestor, and you don't even know it yet. The cards are reminding you of the ancient Hermetic principle 'As above, so below', which is based on the belief that we are capable of bringing forth miracles into our physical reality by tapping into the power of our superconsciousness, or our higher selves. So, how and where would you like to bring about a shift? Will you live a mundane existence or align yourself with the virtue of greatness? It's time to make a choice and commit to it.

Cosmic tip: Tap into the power of the superconsciousness.
'''

	elif Choice==4:
		Forecast='''
Cancer Horoscope:

It's a 'thoughts to things' kind of day in the Cancer HQ, and you're ready to put your wonderful ideas into action. Trust that the Universe is propelling you forward and creating a conducive environment for the manifestation of your dreams. Now is not the time to second guess yourself. Know that you're being guided by your higher self to make the right decisions at the right time. Remember, your swiftness will redefine the game for you.

Cosmic tip: There’s no need to second guess your decisions.
'''

	elif Choice==5:
		Forecast='''
Leo Horoscope:

Leo, you are stepping into a new cycle, one that requires you to embrace your power fully and acknowledge the gifts you've been blessed with. No more playing it small. It's time to give that cloak of invisibility the send-off it deserves. There are three more months for you to achieve the things that you’d set out to earlier this year. Yes, you will be faced with challenges. Keeping in mind that the road to success is paved with failures will help you triumph over them.

Cosmic tip: A 2.0 version of you is emerging from the ashes of the old one.
'''

	elif Choice==6:
		Forecast='''
Virgo Horoscope:

Monday sees you shifting your gaze from the material plane to one that is synonymous with inner illumination. The world of mysteries has your attention, Virgo. You are feeling inspired to delve deeper into your superconsciousness and uncover the gifts of your soul. The path of self-learning will prove to be rewarding for you. Recently been initiated into the world of magick? Consider studying about ancient art and exploring the idea of Quantum physics.

Cosmic tip: It's time to discover your own magick.
'''

	elif Choice==7:
		Forecast='''
Libra Horoscope:

We're never really prepared for what life is about to bring our way, yet we are. You have been working towards this moment for lifetimes, Libra. Don't waste a minute doubting yourself. What you want to do instead: jump into action mode and allow the world to see the most glorious version of you. Standing in your power will set the stage for positive change. For some of you, a new project may be in the pipeline. Trust that the Universe is helping you make your dreams come true.

Cosmic tip: Step into your power.
'''

	elif Choice==8:
		Forecast='''
Scorpio Horoscope:

The planning and strategising stage is over, Scorpio. It's time to get into action mode. Keep your vision in mind as you move forward, and vow to not deviate from the grand plan. You've got this! The Universe is playing on your team too by creating a conducive environment for your growth. It's all about working with the masculine, or the yang force within, which is connected to the energy of the Sun. Consider going for a run in the morning and practicing surya namaskars in your backyard. This will activate your life force and help you go after your dreams with courage and conviction.

Cosmic tip: Get into action mode.
'''

	elif Choice==9:
		Forecast='''
Sagittarius Horoscope

Monday mood: building an empire, creating art, making magic, living consciously, and inspiring those around you to achieve their highest potential. You are more *you* than you have ever been, Sagittarius. You're shining your light on the world like never before. But that doesn't mean the road ahead won't come with its fair share of challenges. When you find yourself wanting to give up, reflect upon Robin Sharma's words: “Trials can be teachers. Hardship can breed heroism. Pain can morph into power. It’s all your choice.”

Cosmic tip: You are building a new life for yourself.
'''

	elif Choice==10:
		Forecast='''
Capricorn Horoscope:

That life on the earthly realm is synonymous with trials and tribulations is not news to you, Capricorn. Challenge yourself to look beyond the chaos and find underlying order anyway. Letting go of your attachment to a specific outcome will help you stay present. As such, flexibility is a superpower that will help you wiggle your way out of the trickiest of situations. So let go of rigidity in any and all forms, and be receptive to what the Universe has to say.

Cosmic tip: It's always easier to flow with the current rather than against it.
'''

	elif Choice==11:
		Forecast='''
Aquarius Horoscope:

'As above, so below' from the Hermetic texts is a principle that accurately describes where you are in your soul's journey, Aquarius. Big manifestation energy surrounds you—and you are witnessing your desires take form in your physical reality. Let this shift inspire you to co-create with the mysterious forces above. Remember, your intention is the most powerful tool at your disposal. So, dream in HD and cast your spell with unyielding faith!

Cosmic tip: Big manifestation energy surrounds you.
'''

	elif Choice==12:
		Forecast='''
Pisces Horoscope:

Dream a little dream, Pisces, and while you're astral travelling through the subtle realms, write us a love song. Taking flights of fantasy is going to be a big theme for you today, and no, that's not a bad thing at all. In fact, the cards are urging you to step back from the chaos and commotion of the outside world in order to surrender to your creative process. Will your time out lead to massive revelations? Yes and no. But the outcome is not something you're meant to attach yourself to.

Cosmic tip: Dream a little dream, my loves.
'''

	if Forecast!=False:
		print(f'{Forecast}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	else:
		print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Enter the Valid Input!!!\a~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
		continue

	i=int(input('To Continue with another Zodiac Press "1" else "0" to Exit:'))
	if i==1:
		continue
	else:
		exit('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Thank You~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\a')
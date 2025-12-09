"""
Configuration des sources à scraper pour le projet LLM.

Pour ajouter une nouvelle source:
1. Ajoutez un nouveau dictionnaire dans la liste SOURCES_CONFIG
2. Format: {
    "url": "https://...",           # URL de la page à scraper
    "nom_fichier": "nom.txt",       # Nom du fichier de sortie (sera dans src/data/)
    "description": "Description"    # Description optionnelle
}
"""

SOURCES_CONFIG = [
    {
        "url": "https://en.wikipedia.org/wiki/Golf",
        "nom_fichier": "golfWikipedia.txt",
        "description": "Introduction au Golf"
    },
    {
        "url": "https://en.wikipedia.org/wiki/Golf_course",
        "nom_fichier": "golfCourseWikipediaCourse.txt",
        "description": "Parcours de Golf"
    },
    {
        "url": "https://en.wikipedia.org/wiki/Professional_Golfers%27_Association_of_America",
        "nom_fichier": "golfPGA.txt",
        "description": "PGA - Association des golfeurs professionnels"
    },
    {
        "url": "https://www.usga.org/content/usga/home-page/rules-hub/amateur-status/amateur-status-modernization/rule-1.html",
        "nom_fichier": "golfRulesFromUSGA1.txt",
        "description": "Règles de Golf - USGA"
    },
    {
        "url": "https://www.usga.org/content/usga/home-page/rules-hub/amateur-status/amateur-status-modernization/rule-2.html",
        "nom_fichier": "golfRulesFromUSGA2.txt",
        "description": "Règles de Golf - USGA"
    },
    {
        "url": "https://www.usga.org/content/usga/home-page/rules-hub/amateur-status/amateur-status-modernization/rule-3.html",
        "nom_fichier": "golfRulesFromUSGA3.txt",
        "description": "Règles de Golf - USGA"
    },
    {
        "url": "https://www.usga.org/content/usga/home-page/rules-hub/amateur-status/amateur-status-modernization/rule-4.html",
        "nom_fichier": "golfRulesFromUSGA4.txt",
        "description": "Règles de Golf - USGA"
    },
    {
        "url": "https://www.usga.org/content/usga/home-page/rules-hub/amateur-status/amateur-status-modernization/rule-5.html",
        "nom_fichier": "golfRulesFromUSGA5.txt",
        "description": "Règles de Golf - USGA"
    },
    {
        "url": "https://www.usga.org/content/usga/home-page/rules-hub/amateur-status/amateur-status-modernization/rule-6.html",
        "nom_fichier": "golfRulesFromUSGA6.txt",
        "description": "Règles de Golf - USGA"
    },
    {
        "url": "https://www.randa.org/rog/the-rules-of-golf",
        "nom_fichier": "golfRulesFromRanda.txt",
        "description": "Règles de Golf - Randa"
    },
    {
        "url": "https://www.randa.org/rog/definitions",
        "nom_fichier": "golfDefinitionsFromRanda.txt",
        "description": "Définitions - Randa"
    },
    {
        "url": "https://www.randa.org/rog/clarifications",
        "nom_fichier": "golfClarificationsFromRanda.txt",
        "description": "Clarifications - Randa"
    },
    {
        "url": "https://www.randa.org/en/rules/rules-hub",
        "nom_fichier": "golfRulesFromRandaHub.txt",
        "description": "Règles de Golf - Randa"
    },
    {
        "url": "https://www.worldgolfmuseum.com/",
        "nom_fichier": "golfRulesFromWorldGolfMuseum.txt",
        "description": "Règles de Golf - World Golf Museum"
    },
    {
        "url": "https://www.sportingheritage.org.uk/content/collection/british-golf-museum",
        "nom_fichier": "golfDefinitionsFromBritishGolfMuseum.txt",
        "description": "Définitions - British Golf Museum"
    },
    {
        "url": "https://www.owgr.com/",
        "nom_fichier": "golfClarificationsFromOWGR.txt",
        "description": "Clarifications - OWGR"
    },
    {
        "url": "https://www.owgr.com/federation-ranking",
        "nom_fichier": "golfRulesFromOWGR.txt",
        "description": "Règles de Golf - OWGR"
    },

    {
        "url": "https://www.europeantour.com/dpworld-tour/stats/records-and-achievements/",
        "nom_fichier": "golfRulesFromEuropeanTour.txt",
        "description": "Règles de Golf - European Tour"
    },
    {
        "url": "https://www.pgatour.com/news",
        "nom_fichier": "golfDefinitionsFromPGATour.txt",
        "description": "Définitions - PGA Tour"
    },
    {
        "url": "http://www.golfinstruction.com/golf-instruction/golf-tips-rotary-swing-lesson-4897.htm",
        "nom_fichier": "golfClarificationsFromGolfInstruction.txt",
        "description": "Clarifications - Golf Instruction"
    },
    {
        "url": "https://rotaryswing.com/golf-instruction/golf-instruction-articles-rs1",
        "nom_fichier": "golfRulesFromRotarySwing.txt",
        "description": "Règles de Golf - Rotary Swing"
    },
    {
        "url": "https://golftec.com/optimotion",
        "nom_fichier": "golfRulesFromGolfTec.txt",
        "description": "Règles de Golf - GolfTec"
    },
    {
        "url": "https://thehiveindex.com/communities/the-hackers-paradise/",
        "nom_fichier": "golfDefinitionsFromTheHackersParadise.txt",
        "description": "Définitions - The Hackers Paradise"
    },
    {
        "url": "https://thehiveindex.com/topics/golf/",
        "nom_fichier": "golfClarificationsFromTheHackersParadise.txt",
        "description": "Clarifications - The Hackers Paradise"
    },
    {
        "url": "https://golf.fandom.com/wiki/Golf",
        "nom_fichier": "golfRulesFromGolfFandom.txt",
        "description": "Règles de Golf - Golf Fandom"
    },
    {
        "url": "https://www.reddit.com/r/golf/comments/1j6iwu/my_beginners_guide_to_golf_includes_lots_of/",
        "nom_fichier": "golfRulesFromReddit.txt",
        "description": "Règles de Golf - Reddit"
    },
    {
        "url": "https://www.reddit.com/r/golf/new/",
        "nom_fichier": "golfDefinitionsFromReddit.txt",
        "description": "Définitions - Reddit"
    },
    {
        "url": "https://www.australiangolfdigest.com.au/reddit-golf-content-of-the-week-everyone-lying-about-how-good-they-are/",
        "nom_fichier": "golfClarificationsFromReddit.txt",
        "description": "Clarifications - Reddit"
    },
    {
        "url": "https://www.golfsidekick.com/knowledge/basic-rules-of-golf-for-beginners/",
        "nom_fichier": "golfRulesFromGolfSidekick.txt",
        "description": "Règles de Golf - Golf Sidekick"
    },
    {
        "url": "https://www.reddit.com/r/golf/comments/wigjyv/what_are_the_unwritten_rules_of_golf_that_you/",
        "nom_fichier": "golfRulesFromReddit2.txt",
        "description": "Règles de Golf - Reddit"
    },
    {
        "url": "https://www.redbull.com/us-en/golf-rules-explained",
        "nom_fichier": "golfDefinitionsFromRedBull.txt",
        "description": "Définitions - Red Bull"
    },
    {
        "url": "https://www.oakridgegolfclub.co.uk/understanding-golf-rules-for-beginners/",
        "nom_fichier": "golfClarificationsFromOakridgeGolfClub.txt",
        "description": "Clarifications - Oakridge Golf Club"
    },
    {
        "url": "https://stix.golf/en-fr/blogs/rough-thoughts/golf-rules-made-simple-a-beginner-s-guide-to-golf-rules-and-etiquette?srsltid=AfmBOoryZBTONInHRrg8BWIvKTehCCbmit_WggEGx90L8UKUzN55EKB6",
        "nom_fichier": "golfRulesFromStix.txt",
        "description": "Règles de Golf - Stix"
    },
    {
        "url": "https://sevenbridgesgolfclub.com/golf-etiquette-for-beginners/",
        "nom_fichier": "golfEtiquetteFromSevenBridges.txt",
        "description": "Étiquette de Golf - Seven Bridges"
    },
    {
        "url": "https://theleftrough.com/rules-of-golf/",
        "nom_fichier": "golfRulesFromTheLeftRough.txt",
        "description": "Règles de Golf - The Left Rough"
    },
    {
        "url": "https://vistabellagolf.com/en/5-basic-golf-rules-every-beginner-should-know/",
        "nom_fichier": "golfRulesFromVistaBella.txt",
        "description": "Règles de Golf - Vista Bella"
    },
    {
        "url": "https://xgolfrockwall.com/golf-rules-for-beginners-x-golf-rockwall/",
        "nom_fichier": "golfRulesFromXGolfRockwall.txt",
        "description": "Règles de Golf - X Golf Rockwall"
    },
    {
        "url": "https://www.stonegategolf.com/blog/36-beginner-guide-golf-rules-etiquette/",
        "nom_fichier": "golfRulesFromStonegateGolf.txt",
        "description": "Règles de Golf - Stonegate Golf"
    },
    {
        "url": "https://mygolfspy.com/news-opinion/instruction/understanding-the-rules-a-beginners-guide-to-golfs-core-principles/",
        "nom_fichier": "golfRulesFromMyGolfSpy.txt",
        "description": "Règles de Golf - My Golf Spy"
    },
    {
        "url": "https://blog.golfnow.com/golf-etiquette-rules-for-beginners/",
        "nom_fichier": "golfEtiquetteFromGolfNow.txt",
        "description": "Étiquette de Golf - Golf Now"
    },
    {
        "url": "https://eynesburygolf.com.au/golf-for-beginners-your-guide-to-the-game/",
        "nom_fichier": "golfForBeginnersFromEynesbury.txt",
        "description": "Golf pour Débutants - Eynesbury"
    },
    {
        "url": "https://www.sportmember.co.uk/en/sports-rules/golf-rules-for-beginners",
        "nom_fichier": "golfRulesForBeginnersFromSportMember.txt",
        "description": "Règles de Golf pour Débutants - Sport Member"
    },
    {
        "url": "https://blog.visitacostadelsol.com/en/golf-for-beginners-basic-rules-and-terms-for-playing-golf",
        "nom_fichier": "golfForBeginnersFromCostaDelSol.txt",
        "description": "Golf pour Débutants - Costa Del Sol"
    },
    {
        "url": "https://justgolfstuff.ca/blogs/guide/golf-rules?srsltid=AfmBOop_EfSfsBllAAL5ApQQZyNRe5GU0Jdt4Qml0QJ1fDQjw0IliYof",
        "nom_fichier": "golfRulesFromJustGolfStuff.txt",
        "description": "Règles de Golf - Just Golf Stuff"
    },
    {
        "url": "https://redlandsmesa.com/essential-rules-and-golf-basics-for-beginners/",
        "nom_fichier": "golfBasicsFromRedlandsMesa.txt",
        "description": "Règles et Bases du Golf - Redlands Mesa"
    },
    {
        "url": "https://www.wikihow.com/Play-Golf",
        "nom_fichier": "golfBasicsFromWikiHow.txt",
        "description": "Comment Jouer au Golf - WikiHow"
    },
    {
        "url": "https://www.olympics.com/en/news/golf-rules-regulations-for-olympics-beginners-guide",
        "nom_fichier": "golfRulesFromOlympics.txt",
        "description": "Règles de Golf - Olympics"
    },
    {
        "url": "https://www.ffgolf.org/tutos-de-l-academie/swing?gad_source=1&gad_campaignid=20388477783&gbraid=0AAAAApVIAypvpoEIpw9auRwl6PIl_giNG&gclid=CjwKCAiAxc_JBhA2EiwAFVs7XMcP7T8rbM6bor0D2MZ0HkfsHrm9nghANGn3drT6XAN3TeEGi_RcnxoCwTUQAvD_BwE",
        "nom_fichier": "golfSwingFromFFGolf.txt",
        "description": "Swing de Golf - FF Golf"
    },
    {
        "url": "https://theleftrough.com/golf-etiquette/",
        "nom_fichier": "golfEtiquetteFromTheLeftRough.txt",
        "description": "Étiquette de Golf - The Left Rough"
    },
    {
        "url": "https://www.golfdigest.com/gallery/golf-beginners-tips",
        "nom_fichier": "golfTipsFromGolfDigest.txt",
        "description": "Conseils de Golf pour Débutants - Golf Digest"
    },
    {
        "url": "https://www.golfzonleadbetter.com/blogs/golf-etiquette/",
        "nom_fichier": "golfEtiquetteFromGolfZonLeadbetter.txt",
        "description": "Étiquette de Golf - GolfZon Leadbetter"
    },
    {
        "url": "https://www.golfpass.com/travel-advisor/articles/5-rules-every-beginning-golfer-should-know",
        "nom_fichier": "golfRulesFromGolfPass.txt",
        "description": "Règles de Golf - Golf Pass"
    },
    {
        "url": "https://www.nationalclubgolfer.com/rules/key-golf-rules-for-beginners/",
        "nom_fichier": "golfRulesFromNationalClubGolfer.txt",
        "description": "Règles de Golf - National Club Golfer"
    },
    {
        "url": "https://www.ffgolf.org/golf-amateur/competitions-des-clubs/calendriers-resultats",
        "nom_fichier": "golfCompetitionsFromFFGolf.txt",
        "description": "Compétitions de Golf - FF Golf"
    },
    {
        "url": "https://shotscope.com/blog/practice-green/game-improvement/a-beginners-guide-to-golf-everything-you-need-to-know/",
        "nom_fichier": "golfBeginnersGuideFromShotScope.txt",
        "description": "Guide du Débutant au Golf - Shot Scope"
    },
    {
        "url": "https://www.golfhouse.com/general-knowledge-golf.htm",
        "nom_fichier": "golfGeneralKnowledgeFromGolfHouse.txt",
        "description": "Connaissances Générales sur le Golf - Golf House"
    },
    {
        "url": "https://deercreekflorida.com/blog/articles/beginners-guide-to-golf",
        "nom_fichier": "golfBeginnersGuideFromDeerCreek.txt",
        "description": "Guide du Débutant au Golf - Deer Creek"
    },
    {
        "url": "https://englandigolf.co.uk/igolf-blog/how-to-play-golf-a-beginners-guide/",
        "nom_fichier": "golfBeginnersGuideFromEnglandIGolf.txt",
        "description": "Guide du Débutant au Golf - England iGolf"
    },
    {
        "url": "https://stix.golf/en-fr/blogs/rough-thoughts/100-beginner-golfer-questions-answered?srsltid=AfmBOorIT2QFDcQ3kGy6wVtpb-TTfgQufx4DQYA9XLBf9sck9aPD0b9Y",
        "nom_fichier": "golfBeginnerQuestionsFromStix.txt",
        "description": "100 Questions pour Golfeurs Débutants - Stix"
    },
    {
        "url": "https://stix.golf/en-fr/blogs/rough-thoughts/100-beginner-golfer-questions-answered?srsltid=AfmBOoramekxk03AGA_OqQjkkP5u19mnoD215n0yMYaBb-gCJ-vhDz2h",
        "nom_fichier": "golfBeginnerQuestionsFromStix.txt",
        "description": "100 Questions pour Golfeurs Débutants - Stix"
    },
    {
        "url": "https://gulfnews.com/sport/golf-in-uae/the-complete-beginners-guide-to-understanding-golf-1.1660828",
        "nom_fichier": "golfBeginnersGuideFromGulfNews.txt",
        "description": "Guide du Débutant au Golf - Gulf News"
    },
    {
        "url": "https://blog.ncga.org/5-things-to-know-before-your-first-round-of-golf",
        "nom_fichier": "golfFirstRoundFromNCGA.txt",
        "description": "5 Choses à Savoir Avant Votre Première Partie de Golf - NCGA"
    },
    {
        "url": "https://www.golfdigest.com/story/the-complete-beginner-s-guide-to-golf",
        "nom_fichier": "golfBeginnersGuideFromGolfDigest.txt",
        "description": "Guide du Débutant au Golf - Golf Digest"
    }
]
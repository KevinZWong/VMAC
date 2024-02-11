import re


class ScriptProcessing:
    def __init__(self):
        pass
    def ScriptSpliterV2(self, input_text): # for script
        # split the text into sentences
        sentences = re.split('(?<=[.!?]) +', input_text)

        segments = []
        current_segment = []

        for sentence in sentences:
            words = sentence.split()

            # if a sentence has more than 15 words, split it further
            if len(words) > 15:
                i = 0
                while i < len(words):
                    if len(current_segment) + len(words[i:i+15]) <= 15:
                        current_segment += words[i:i+15]
                        i += 15
                    else:
                        segments.append(' '.join(current_segment))
                        current_segment = []
            else:
                if len(current_segment) + len(words) <= 15:
                    current_segment += words
                else:
                    segments.append(' '.join(current_segment))
                    current_segment = words

        # add the last segment if it exists
        if current_segment:
            segments.append(' '.join(current_segment))

        # if a segment has less than 4 words, combine it with a neighboring segment
        i = 0
        while i < len(segments):
            if len(segments[i].split()) < 4:
                if i != 0: # if it's not the first segment, combine with the previous one
                    segments[i-1] = segments[i-1] + ' ' + segments[i]
                    del segments[i]
                elif i != len(segments) - 1: # if it's not the last segment, combine with the next one
                    segments[i] = segments[i] + ' ' + segments[i+1]
                    del segments[i+1]
            i += 1

        return segments
    def titleFormater(self, title, rowWordCount):
        title = title.split()
        titleWordCounter = 0
        FinalTitle = ""
        for j,v in enumerate(title):
            if titleWordCounter == rowWordCount or v == len(title)-1:
                FinalTitle += "\n"
                titleWordCounter = 0
            FinalTitle += v + " "
            titleWordCounter += 1
        return FinalTitle
    
    def imageScriptGen(self, data):
        title = data[0]
        script = data[1]

        segments = re.split('(?<=[.!?]) +', script)
        stitchedSegments = []
        segList = []
        for seg in segments:
            tempList = seg.split()
            for word in tempList:
                segList.append(word)
            if len(segList) >= 15:
                stitch = ""
                for i in segList:
                    stitch += i + " "
                stitchedSegments.append(stitch)
                segList = []
        stitchedSegments.insert(0, title)
        return stitchedSegments
if __name__ == "__main__":    
    obj1 = ScriptProcessing()

    data = [['Artificial intelligence in healthcare', "Yo, let's talk about artificial intelligence in healthcare, cuz that shit's mind-blowing! So, check this out. Did you know that AI can now help doctors diagnose illnesses better than some puny human brains? Yeah, fuckin' incredible, right? AI algorithms analyze tons of medical data to identify patterns and predict diseases with insane accuracy. It's like having a super smart 'puter that's seen a gazillion patients and knows all the fuckin' symptoms and shit. And here's the sickest part: it doesn't get tired or make dumbass mistakes like us mortals! This AI tech is like the ultimate sidekick for doctors, helping them not only diagnose but also personalize treatment plans for patients. It's revolutionizing the healthcare game, man. Can you fuckin' imagine a world where AI assists in preventing diseases before they even fuckin' happen? Well, it's slowly becoming a reality, my friend. With its ability to analyze massive amounts of data from patients, genetics, and even wearable devices, AI is helping healthcare professionals make better decisions and save lives. So, forget those old-school diagnoses, bro, 'cause AI is the new fuckin' boss in town!"], [' Impact of climate change on marine life', 'Dude, let me tell you something mind-blowing about the impact of climate change on marine life. So, picture this: our lovely oceans, right? They\'re home to all sorts of living creatures, from tiny vibrant coral polyps to ginormous humpback whales. But here\'s the thing, my friend, climate change is like a freakin\' tsunami smashing into their homes and screwing everything up. See, as the planet heats up, ocean temperatures are rising faster than you can say "hot damn!" And guess what? That\'s messing with the whole ecosystem down there. Some marine species, like the adorable clownfish, can\'t handle the heat and are forced to move to cooler areas, basically becoming underwater climate refugees. But that\'s not all, bro. Higher water temperatures are making these badass corals go all "I\'m outta here" and they\'re bleaching like mad. And let me tell you, coral bleaching is not the bucket of sunshine you\'d imagine. It\'s like watching a rainbow turn monochrome because the corals are losing their vibrant colors and basically dying off. Now, if those corals kick the bucket, it\'s not just them waving us a big "F*ck you!" It\'s also the whole damn food chain screaming "Kaput!" You see, corals are like the rockstars of the ocean, providing food and safe havens for a gazillion other marine species. So, if these coral reefs crumble, and their vibrant communities collapse, it\'s like we\'ve just shot ourselves in the foot, bro. But hey, here\'s the kicker, if we manage to get our sh*t together and tackle climate change head-on, we may still have a chance to save our marine buddies. So let\'s all drop our excuses and get on this, because we\'re in this together, man! Peace out.']]

    print(obj1.imageScriptGen(data[0]))




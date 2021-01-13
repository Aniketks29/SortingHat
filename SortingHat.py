
def sortByAlpha(l):
    n = len(l)
    for k in range(0, n - 2):
        for i in range(1, n - k):
            j = 0
            while (True):
                n1 = len(l[i - 1])
                n2 = len(l[i])
                if (j >= n1 or j >= n2):
                    break
                if l[i - 1][j].lower() > l[i][j].lower():
                    temp = l[i - 1]
                    l[i - 1] = l[i]
                    l[i] = temp
                    break
                j += 1
    return l 


    
if __name__ == "__main__":
    hackathons = {"CruzHacks" : "01/15/2021",
                  "Elle Hacks" : "01/15/2021",
                  "Hack the Northeast Beyond" : "01/15/2021",
                  "SB Hacks" : "01/15/2021",
                  "HackDavis" : "01/16/2021",
                  "Rose Hack" : "01/16/2021",
                  "BoilerMake" : "01/22/2021",
                  "Hack Your Portfolio" : "01/22/2021",
                  "QHacks" : "01/22/2021",
                  "TechTogether Seattle" : "01/22/2021",
                  "CUNY Hackathon" : "01/23/2021",
                  "Hack@Brown" : "01/23/2021",
                  "Hex Cambridge 2021" : "01/23/2021",
                  "QWER Hacks" : "01/23/2021",
                  "cuHacking" : "01/29/2021",
                  "Hoya Hacks" : "01/29/2021",
                  "Swamp Hacks" : "01/29/2021",
                  "Chackit" : "01/30/2021",
                  "HackViolet" : "01/30/2021",
                  "Hacklytics" : "02/5/2021",
                  "KU HackFest 2021" : "02/19/2021",
                  "Pearl Hacks" : "02/19/2021",
                  "BrickHack 7" : "02/20/2021",
                  "StormHacks" : "02/20/2021"
                  }

    print("Sort Alphabetically: ")
    lis_key = [key for key in hackathons.keys()]

    print(sortByAlpha(lis_key))

        



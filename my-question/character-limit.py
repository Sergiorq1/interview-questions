# Question
# Given a character limit and a sentence, return a new sentence with “ % ”  separating each character limit 

# Input
# test input: 280, 'Federal Reserve policymakers scaled back their expectations for rate hikes this year after a series of bank collapses roiled markets last month, and stressed they would remain vigilant for the potential of a credit crunch to further slow the economy, a record of the meeting showed. “Many participants noted that the likely effects of recent banking-sector developments on economic activity and inflation had led them to lower their assessments of the federal funds rate target range that would be sufficiently restrictive,” according to minutes of the March 21-22 Federal Open Market Committee gathering, released in Washington Wednesday.'

class Solution:
    def character_limit(self, limit:int, sentence:str):
        #For loop that loops at every 
        for char in range(len(sentence)):
            print(sentence[char])

sol = Solution()
print(sol.character_limit(280, 'Federal Reserve policymakers scaled back their expectations for rate hikes this year after a series of bank collapses roiled markets last month, and stressed they would remain vigilant for the potential of a credit crunch to further slow the economy, a record of the meeting showed. “Many participants noted that the likely effects of recent banking-sector developments on economic activity and inflation had led them to lower their assessments of the federal funds rate target range that would be sufficiently restrictive,” according to minutes of the March 21-22 Federal Open Market Committee gathering, released in Washington Wednesday.'))
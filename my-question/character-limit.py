# Question
# Given a character limit and a sentence, return a new sentence with “ % ”  separating each character limit 

# Example 1

# input: 280, 'Federal Reserve policymakers scaled back their expectations for rate hikes this year after a series of bank collapses roiled markets last month, and stressed they would remain vigilant for the potential of a credit crunch to further slow the economy, a record of the meeting showed. “Many participants noted that the likely effects of recent banking-sector developments on economic activity and inflation had led them to lower their assessments of the federal funds rate target range that would be sufficiently restrictive,” according to minutes of the March 21-22 Federal Open Market Committee gathering, released in Washington Wednesday.'

# output: Federal Reserve policymakers scaled back their expectations for rate hikes this year after a series of bank collapses roiled markets last month, and stressed they would remain vigilant for the potential of a credit crunch to further slow the economy, a record of the meeting showed. “Many participants noted that the likely effects  %  of recent banking-sector developments on economic activity and inflation had led them to lower their assessments of the federal funds rate target range that would be sufficiently restrictive,” according to minutes of the March 21-22 Federal Open Market Committee gathering, released in Washington Wednesday.


#Example 2

# input: 50, 'Federal Reserve policymakers scaled back their expectations for rate hikes this year after a series of bank collapses'

# output 
#output: Federal Reserve policymakers scaled back their  %  expectations for rate hikes this year after a series of bank  %  collapses


class Solution:
    def character_limit(self, limit:int, paragraph:str):
        # declare a counter 
        counter = 0
        # split paragraph into list of words
        paragraph_list = paragraph.split()
        # loop through paragraph_list with for loop 
        for word in range(len(paragraph_list)):
            counter += len(paragraph_list[word])
            # if counter equal or greater than limit:
            if counter >= limit:
                # if limit is met at the end of a word:
                if counter == limit:
                    # insert ' % ' inside the paragraph
                    paragraph_list.insert(word+1, ' % ')
                # if counter is greater than limit
                if counter > limit:
                    paragraph_list.insert(word, ' % ')
                # reset counter for next loop
                counter = 0
        #return paragraph
        return ' '.join(paragraph_list)


        

sol = Solution()
#Twitter's character limit is 280
print(sol.character_limit(50, 'Federal Reserve policymakers scaled back their expectations for rate hikes this year after a series of bank collapses'))
print(sol.character_limit(280, 'Federal Reserve policymakers scaled back their expectations for rate hikes this year after a series of bank collapses roiled markets last month, and stressed they would remain vigilant for the potential of a credit crunch to further slow the economy, a record of the meeting showed. “Many participants noted that the likely effects of recent banking-sector developments on economic activity and inflation had led them to lower their assessments of the federal funds rate target range that would be sufficiently restrictive,” according to minutes of the March 21-22 Federal Open Market Committee gathering, released in Washington Wednesday.'))
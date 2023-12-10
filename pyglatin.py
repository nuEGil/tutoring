
def to_piglatin(words):
    # so this function assumes that I have a list of words to play with
    # see the actions in the main statments
    platins = []
    for item in words:
        #since this is python2 I need to explicitly make a list from the string
        lword = list(item)

        # Here I do a list comprehension. So I'm saving the index and the vowel of
        # the first voel that occurs in the word. I save that as a list of
        # tuples fv

        fv = [(ind,lett) for ind,lett in enumerate(lword) if lett in 'aeiouyAEIOUY']

        first_index  = fv[0][0]
        first_letter = fv[0][1]
        print(item, fv[0])
        # so  if the first letter is a vowel, I just add ay to the end of it.
        if lword[0] in 'aeiouyAEIOUY':
            platin = ''.join(lword)+'ay'
            print(platin)
            platins.append(platin)
        # if the first letter is not a vowel then I need to use my fv variable
        # so the variable on line 16 : first
        # this will let us copy the first few letters and add it to the end of the
        # list
        else:
            #we are going to make what is called a circular buffer.
            #so we save the last part of the list and scoot it over, then add
            #a new letter to the end. in this case the new letter is then
            #first letter


            # save the first few letters of the word
            flett = lword[0:first_index]
            print(flett)
            # next scoot the last few letters over
            lword[0:-first_index] = lword[first_index::]
            lword[-first_index::] = flett
            print(lword)

            platin = ''.join(lword)+'ay'
            print(platin)
            platins.append(platin)

    return platins

if __name__ == "__main__":
    # here is where we are going to write our main code
    # initialize a word list to play with
    words = ['pig','cow','september','shoe',
            'start','apple','chrisanthemum',
            'ygdrasil']
    # be sure to mute any unwanted print messages in this file with a pound sign
    platin = to_piglatin(words)
    print('final answer: {}'.format(platin))

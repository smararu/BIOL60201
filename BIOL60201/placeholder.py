#CONSTANTS
#filelocation instead of DNA
DNA = "tttatggcaattaaaattggtatcaatggttttggtcgtatcggccgtatcgtattctagttttttttttttatggcaattaaaattggtatcaatggttttggtcgtatcggccgtatcgtattctagttttttttt"
START_CODON = ['atg']
STOP_CODON = = ['tga' , 'tag' , 'taa']

DNALength = DNA.lenght()

#Shift frames function
def shift_left(lst, n):
    """Shifts the lst over by n indices

    >>> lst = [1, 2, 3, 4, 5]
    >>> shift_left(lst, 2)
    >>> lst
    [3, 4, 5, 1, 2]
    """
    if n < 0:
    	raise ValueError("Input %d is not a non-negative integer" % n)

   	if n == 0:
    	return
	else:
    	lst = lst[1:] + [lst[0]]
    	shift_left(lst, n-1)


def readDNA(framelength, DNALength):
	
def shift_right(lst, n):
    """Shifts the lst over by n indices

    >>> lst = [1, 2, 3, 4, 5]
    >>> shift_right(lst, 2)
    >>> lst
    [4, 5, 1, 2, 3]
    """
    if n < 0:
    	raise ValueError("Input %d is not a non-negative integer" % n)

   	if n == 0:
    	return
	else:
		lst = lst[len(lst)-1:] + lst[:len(lst)-1]
    	shift_right(lst, n-1)



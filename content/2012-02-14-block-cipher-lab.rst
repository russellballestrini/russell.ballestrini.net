Block cipher lab
################
:date: 2012-02-14 01:36
:author: Russell Ballestrini
:tags: Code, Security
:slug: block-cipher-lab
:status: published

| 
|  **Consider the following block cipher.** Suppose that each block
  cipher T simply reverses the order of the eight input bits (so that,
  for example 11110000 becomes 00001111).
|  Further suppose that the 64-bit scrambler does not modify any bits.
  With n = 3 iterations and the original 64-bit input equal to 10100000
  repeated eight times, what is the value of the output?
|  Now change the last bit of the original 64-bit input from 0 to a 1.
  Now suppose that the 64-bit scrambler inverses the order of the 64
  bits.
|  **Solution in python:**

::

    def chunks( l, n ):
        """accept a list and chuck size, return chunks"""
        return [ l[ i:i+n ] for i in range( 0, len(l), n ) ]


    def T( blocks ):
        """for each block, reverse block, return blocks"""
        result = []
        for block in blocks:
            result.append( ''.join( [bit for bit in reversed( block )] ) )

        return result

    def scrambler( input ):
        """inverse the order of input"""
        return ''.join( [i for i in reversed( input ) ] )


    def cipher1( input, n = 3, chunk_length = 8 ):
        """make chucks out of input, reverse each chunk return result"""
        blocks = chunks( input, chunk_length )
        for i in range( 0, n ): blocks = T( blocks )
        return ''.join( blocks )


    def cipher2( input, n = 3, chunk_length = 8 ):
        """same as cipher1 but with scrambler"""
        blocks = chunks( input, chunk_length )
        for i in range( 0, n ):
            blocks = T( blocks )
            blocks = chunks( scrambler( ''.join( blocks ) ), chunk_length )
        return ''.join( blocks )


    if __name__ == "__main__":

        input = "1010000010100000101000001010000010100000101000001010000010100000"
        print cipher1( input )
        # output: 0000010100000101000001010000010100000101000001010000010100000101

        input = "1010000010100000101000001010000010100000101000001010000010100001"
        print cipher1( input )
        # output: 0000010100000101000001010000010100000101000001010000010110000101

        input = "1010000010100000101000001010000010100000101000001010000010100000"
        print cipher2( input )
        # output: 1010000010100000101000001010000010100000101000001010000010100000

        input = "1010000010100000101000001010000010100000101000001010000010100001"
        print cipher2( input )
        # output: 1010000110100000101000001010000010100000101000001010000010100000

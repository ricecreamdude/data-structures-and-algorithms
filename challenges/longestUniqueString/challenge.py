class Solution:
    def lengthOfLongestSubstring(self, s):
        output = 0
        track = ""
        for char in s:
            if char in track:
                while True:
                    #
                    if track[0] == char:
                        track = track[1:]
                        track += char
                        break
                    #If the character is found in 'track', remove the first character from track until
                    #char == track[0].  Once the character is removed, you are at the beginning of the
                    #next longest string
                    else:
                        track = track[1:]
            else:
                track += char
            #Regardless of the current length of track, the longest length of track will be stored here
            #and returned as your answer.
            if len(track) > output:
                output = len(track)
        print('track:', track)
        return output
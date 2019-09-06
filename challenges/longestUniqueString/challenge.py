class Solution:
    def lengthOfLongestSubstring(self, s):
        output = 0
        track = ""
        for char in s:
            if char in track:
                while True:
                    if track[0] == char:
                        track = track[1:]
                        track += char
                        break
                    else:
                        track = track[1:]
            else:
                track += char
            if len(track) > output:
                output = len(track)
        print('track:', track)
        return output
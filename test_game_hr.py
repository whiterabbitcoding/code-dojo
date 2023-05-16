def minion_game(string):
    # your code goes here
    s = "BNAANA"
    vowels = "AEIOU"
    consonants = "bcdfghjklmnpqrstvwxyz".upper()
    vowel_strings = sorted(
        s[i:j] for i, x in enumerate(s) for j in range(i + 1, len(s) + 1) if x in vowels
    )
    consonant_strings = sorted(
        s[i:j]
        for i, x in enumerate(s)
        for j in range(i + 1, len(s) + 1)
        if x in consonants
    )
    vs = list(dict.fromkeys(vowel_strings))
    cs = list(dict.fromkeys(consonant_strings))
    diff = [s.count(x) for x in vs]
    print(diff)
    max_v = sum([s.count(x) for x in vs])
    max_s = sum([s.count(x) for x in cs])
    print(f"Stuart {max_s}") if max_s > max_v else print(f"Kevin {max_v}")


if __name__ == "__main__":
    s = input()
    minion_game(s)

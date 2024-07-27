class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores_dict = defaultdict(list)

        for ID, score in items:
            scores_dict[ID].append(score)

        res = []

        for ID, scores in scores_dict.items():
            scores.sort(reverse=True)
            top_five = sum(scores[:5]) // 5
            res.append([ID, top_five])
        
        res.sort()
        return res
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make nums dict with numbers and number of times they occur
        nums_dict = {}
        for elem in nums:
            if elem not in nums_dict:
                nums_dict[elem] = 1
            else:
                nums_dict[elem] += 1

        print(nums_dict)
        
        # make list of k most frequent elements
        # running list of 3 with new entries kicking old
        most_frequent = []
        for key,v in nums_dict.items():
            if len(most_frequent) < k:
                most_frequent.append((key,v))
            else:
                #Need to account for deleting the value with the least occurrences 
                #Only need to do it for the element with the least occurrences 
                minimum = min(x[1] for x in most_frequent)
                min_elem = min(most_frequent, key=lambda x: x[1])
                if v > minimum:
                    most_frequent.remove(min_elem)
                    most_frequent.append((key,v))
                # for elem in most_frequent:
                #     if v > elem[1]:
                #         most_frequent.remove(elem)
                #         most_frequent.append((key,v))
                #         break

            print(most_frequent)

        #now have list of [(k,v),...] with highest values
        #so now make list with just k
        final = []
        for elem in most_frequent:
            final.append(elem[0])
        
        return final
            
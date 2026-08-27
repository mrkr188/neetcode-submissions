class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        email_to_name = {}
        adj = defaultdict(list)

        # build an email-to-email graph and map each email to a name
        for account in accounts:
            name = account[0]
            first_email = account[1]
            email_to_name[first_email] = name
            for email in account[2:]:
                adj[email].append(first_email)
                adj[first_email].append(email)
                email_to_name[email] = name
        
        res = []
        seen = set()
        
        # traverse the graph using DFS
        for email in email_to_name:
            if email in seen:
                continue
                
            stack = [email]
            seen.add(email)
            current_emails = []
            
            while stack:
                curr = stack.pop()
                current_emails.append(curr)
                
                for neighbor in adj[curr]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
                        
            name = email_to_name[email]
            res.append([name] + sorted(current_emails))
        
        return res
                    
                    
                 




            
        
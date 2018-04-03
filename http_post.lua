counter = 100000
request = function()
   path ="/hello"
   counter = counter + 1
   headers = {TH= "application/json"}
   body = string.format('[{"member_id":"%u"}]', counter)
   return wrk.format("POST", path, headers, body)
end

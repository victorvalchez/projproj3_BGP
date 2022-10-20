## Project 3: BGP Router  
 
### Description  
In this project, we implement a simple BGP router. This will help us understand how core internet infrastructure works, by implementing, building and managing forwarding tables, generating route announcements, and forwarding data packets from internet users. 
We will also experience manipulating IP addresses, and make sure to understand subnet mask notation and the purpose of network masks. 
 
### Approach  
We started with the code provided by the professors, which implemented the basic argument manipulation, some dictionaries to store the relations, ports and opened sockets, the sending of the first message _handshake_ to the connected neighbors, and the _our_address_ and _send_ methods to implement basic functionality.
 
Following the order proposed, we implemented the _update_ method, where we store new networks in our forwarding table and send the corresponding update to our connected routers. One thing we implemented is an extra key to check if the network had been aggregated to check whenever a withdrawal happened, also used to disaggregate the table if needed. When an update happens, we check if the updated table can be aggregated.
 
For the _data_ method, we first check if there are any possible networks to send it to, and based on that we differentiate between all the possibilities. In case there is no route, we send that message to the source, if there is one route, we send it there. Otherwise (multiple possible routes), we select the proper one based on the statements tie-breaking rules:
1. The entry with the highest localpref wins.
2. The entry with selfOrigin as true wins.
3. The entry with the shortest ASPath wins.
4. The entry with the best origin wins. Where IGP > EGP > UNK.
5. The entry from the neighbor router (i.e., the src of the update message) with the lowest IP address.
 
Then, we implemented the _dump_ function, which sends the whole forwarding table to the source requesting it (using the _send_ method). It includes the method _show_fields_ which just returns the original fields omitting the ‘aggregable’ one we added for personal convenience.
 
Following, the _withdraw_ method, it is easy to delete the given network from the ‘disaggregated’ table (mentioned in the next paragraph) since we just have to compare both network and netmask and if they match remove it from that table. However, in the ‘aggregated’ table we have to check if that network had been aggregated before to disaggregate the whole table. We do this by applying the current network’s netmask to the withdraw IP to see if they match and then delete it. After this, we restore the table and perform aggregation again if possible.
 
Finally, we implemented route aggregation and disaggregation. To do so, we duplicated our table: in _table_aggregation_ we do this optimization, but we keep a _table_disaggregated_ table, with all the original updates, to restore our aggregated table after a withdraw as we have explained. 
 
The aggregation takes place in our function _is_aggregable_. Given two networks, this function checks if they are aggregable and, in that case, performs the aggregation. The algorithm is easier to explain than to implement:
1. Check if the attributes of both networks are the same. To compare networks, we have to apply the “aggregated” netmask: it is just the original one with the less significant bit different from 0 set to 0 . If that’s the case, networks are aggregable and we continue with the algorithm.
2. Delete one of the entries. After an update, we conserve the new one, which we add at the end, to save us some iterations afterwards.
3. Update the information of the remaining entry: to do so, we work with the binary network and netmask and then we convert it to decimal again. The resulting netmask is the “aggregated” one already mentioned, and the resulting network is just the original one, but with the new netmask applied.
 
We also took into consideration that, when aggregation is applied, a new aggregation may be available with the new entry. That’s why in our _check_aggregation_ functions we restart the loop when this happens.
 
### Challenges and difficulties  
The biggest challenge for us has been understanding the structure of all the data structures we are using, and how to combine them to get the expected output. We wanted to deeply understand how everything was going to work to decide what our table would look like. In the end, we created our table as a dictionary, with the port associated with the network as the key, so we can easily identify all the networks connected to a given port. This increases our efficiency because it narrows the number of networks we have to check to perform aggregation and disaggregation.
 
We also had a really big problem when we duplicated our table (the original one and another one in which we perform aggregation) because we were not taking into consideration the fact that a dictionary is a mutable variable, and so if we try to create a copy just by doing a regular assignment, the result is that both tables are pointing to the same chunk of memory, which implies that our copies are not independent. We had to do some deep debugging to see what was going on because we were taking for granted that the error was not there.
 
### Testing and debugging
Testing has been pretty easy compared to the previous project thanks to all the tests provided. By looking at all the printed information in our terminal, we could figure out exactly what was going on in every test. The only difficulty we experienced was that sometimes it was a little bit confusing to read all the information from the terminal, and in that case, we just took a pen and a piece of paper and started drawing our network. 
 
However, we also noticed that some initial tests were too simple to cover all the possible scenarios, because we got some errors in higher tests related to features implemented in the starter ones. That’s why we complemented our testing by looking at the value of our variables during the whole execution, to see if the behavior was the one we expected.
from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

##res = tavily_search("What is AI")
##print(res)

#res = search_flights("Plan a 7 Days Turkey trip from Riyadh")
#print(res)

user_input = input("Enter travel request: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFINAL RESPONSE:\n")
print(response["answer"])


#Masked
from ntpath import split

mobile_no="9876543210"
masked= mobile_no[:2] + "******" + mobile_no[-2:]
print(masked)

#Formatted

movie_name="viNnai tHandi vaRuvaya"
actor_name="siLambarasan tR"
formatted=f"Movie name is: {movie_name.title()}, Actor name is: {actor_name.title()}"
print(formatted)

location="Villupuram"
fixed_location= location.replace("Villupuram","Madurai")
print(fixed_location)

message="Your Order id is: 1234567. Have a great meal"
order_id=message.split(":")[1].split(".")[0].strip()
print(order_id)

promo_msg="use new100 to get 100 off on your first order"
if "new100" in promo_msg:
    print("offer applied")

feedback="the food was nice and service was good"
print("position is:", feedback.find("service"))

name="vignesh nithya"
initials="".join([word[0].upper() for word in name.split()])
print(initials)


mode_of_transport="          train           "
clean=mode_of_transport.strip()
print(clean)

status="i am learning python basics"
word_count=len(status.split())
print(word_count)


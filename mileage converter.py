print ("How many kilometers did you bike today?")
kms = float(input())

print(f"Ok, you said {kms} kilometers.")

print("We're going to convert that to miles. Ok?")
input()

miles = kms/1.609 	        # Converts kilometers to miles
miles = round(miles, 2)	    # Rounds mile count to 2 significant digits

print(f"You biked {miles} miles!") 
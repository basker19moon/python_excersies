from faker import Faker
fake = Faker()
print('Name', fake.name())
print('Email ', fake.email())
#print(fake.aadhaar_id(556698746228))
print(fake.address())
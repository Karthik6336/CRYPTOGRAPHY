from Crypto.Util import number
import random
import binascii

def rsa():
    # Generate prime numbers p and q
    p = number.getPrime(1024)
    q = number.getPrime(1024)
    
    # Calculate N and phi
    N = p * q
    phi = (p - 1) * (q - 1)
    
    # Generate e such that e and phi are coprime and 0 < e < phi
    e = number.getPrime(512)
    while phi % e == 0 or e >= phi:
        e = number.getPrime(512)
    
    # Calculate d (private key) such that (d * e) % phi == 1
    d = pow(e, -1, phi)
    
    print("Prime number p:", p)
    print("Prime number q:", q)
    print("Public key is:", e)
    print("Private key is:", d)
    
    # User input for plain text
    plain_text = input("Enter the plain text: ")
    print("Encrypting String:", plain_text)

    # Convert the plain text to bytes and encrypt it using public key
    plain_bytes = plain_text.encode('utf-8')
    plain_int = int(binascii.hexlify(plain_bytes), 16)
    
    encrypted = pow(plain_int, e, N)

    # Decrypt the encrypted message using the private key
    decrypted_int = pow(encrypted, d, N)
    decrypted_bytes = hex(decrypted_int)[2:].encode('utf-8')
    
    # Convert the decrypted bytes back to string
    decrypted_text = bytes.fromhex(decrypted_bytes.decode('utf-8')).decode('utf-8')
    
    print("Encrypted Bytes:", list(str(encrypted)))
    print("Decrypted Bytes:", list(decrypted_bytes))
    print("Decrypted String:", decrypted_text)

if __name__ == "__main__":
    rsa()


# Prime number p: 12263235626919408342148523745485648557354327632028537224465498255732896043962051124108482011017534775883745332046234982615039065605713532925814214190457365129831208204640071784536174699757384355618
    4050490466281828769973344421966017885467920013967149068119498878263524777883190201758097707352579883306791280077
# Prime number q: 13240106931182306812870076909122492874043495328026006424774075653104043835678270912159215841758602735922038303109235364216084599713988530086803019548997877851243847342311095971831173451027002878841
    5491738051698437206367468100727988160187305461737138648120761734011844466610968447840302437483472512447359427847
# Public key is: 12617738430879869616724959237576183401486542014219218120367001271427069161833870200398882244829656235699856255558168240726103907407075715930005738882045721
# Private key is: 25192394241023204704157169938842471727873073791948587456458756257328984603283691398368908068284430715680591730481729840857858155205703004859660524100730168037099581677235213270122054720565579466356
    54219214634743205041980392891346928870936822073696403968421490780554026269495712837094584263264048747440935829998721962011588597149900153786259039510484606868910527436687401055699559589492706908624651628157645509
    046798366116238664505724466238693118444565304088559076736751159737730015196572445047417777446010348928971555077399309033612745376745127458905205755868333453876011469678505832943132523790051816126325759178721
# Enter the plain text: abcd  
# Encrypting String: abcd
# Encrypted Bytes: ['6', '4', '1', '7', '7', '1', '8', '3', '2', '3', '1', '4', '9', '8', '2', '1', '6', '2', '4', '5', '7', '7', '9', '2', '8', '2', '3', '8', '2', '3', '5', '4', '7', '1', '7', '1', '9', '4', '7', '0',
    '3', '4', '1', '2', '0', '2', '2', '6', '4', '9', '5', '1', '7', '8', '8', '0', '2', '8', '0', '7', '0', '6', '2', '9', '8', '5', '4', '9', '1', '0', '0', '7', '9', '8', '2', '3', '8', '0', '9', '4', '0', '1', '3', 
    '4', '1', '4', '8', '3', '7', '3', '4', '0', '5', '6', '0', '3', '6', '8', '4', '9', '2', '0', '4', '1', '1', '0', '7', '7', '3', '1', '3', '7', '9', '0', '0', '5', '9', '9', '9', '8', '8', '5', '2', '4', '9', '4',
    '1', '6', '3', '1', '7', '0', '6', '1', '0', '2', '1', '8', '1', '9', '2', '7', '8', '6', '4', '2', '5', '0', '7', '5', '8', '2', '0', '9', '0', '2', '2', '7', '4', '6', '4', '9', '7', '4', '6', '6', '4', '2', '7',
    '3', '3', '7', '5', '3', '8', '6', '2', '4', '5', '7', '2', '1', '5', '8', '2', '7', '3', '2', '2', '0', '0', '1', '2', '7', '8', '4', '3', '7', '7', '9', '4', '6', '1', '8', '9', '3', '3', '6', '2', '2', '7', '4',
    '6', '1', '9', '4', '8', '1', '5', '0', '1', '4', '9', '3', '1', '2', '0', '2', '3', '4', '4', '3', '1', '0', '5', '1', '4', '0', '9', '3', '7', '3', '3', '6', '6', '4', '6', '2', '6', '1', '5', '5', '4', '2', '1',
    '0', '9', '6', '3', '0', '4', '0', '6', '3', '3', '0', '0', '8', '0', '1', '1', '1', '1', '1', '6', '3', '2', '2', '1', '7', '6', '0', '8', '1', '5', '1', '8', '0', '6', '6', '7', '1', '3', '3', '9', '2', '5', '5',
    '7', '6', '1', '9', '5', '7', '7', '8', '3', '6', '6', '9', '9', '7', '9', '9', '5', '6', '9', '7', '8', '0', '9', '0', '3', '6', '6', '3', '2', '3', '4', '8', '5', '3', '7', '7', '3', '4', '0', '4', '3', '8', '5',
    '9', '1', '9', '0', '8', '2', '1', '5', '3', '7', '3', '3', '8', '9', '1', '9', '2', '2', '1', '7', '3', '2', '1', '2', '0', '2', '9', '5', '3', '8', '1', '4', '3', '3', '7', '0', '3', '9', '6', '1', '1', '0', '0', 
    '2', '6', '0', '3', '3', '2', '4', '0', '5', '2', '6', '5', '5', '7', '3', '2', '5', '5', '2', '4', '0', '2', '1', '7', '1', '0', '4', '2', '7', '8', '7', '3', '6', '3', '9', '9', '7', '7', '3', '5', '9', '2', '5',
    '2', '4', '4', '1', '2', '6', '3', '4', '8', '9', '6', '7', '2', '8', '0', '9', '7', '3', '4', '3', '9', '3', '8', '1', '8', '1', '2', '2', '5', '1', '3', '7', '9', '1', '2', '4', '2', '9', '4', '0', '3', '6', '2',
    '9', '7', '2', '9', '2', '8', '2', '8', '2', '8', '1', '1', '7', '3', '7', '8', '2', '3', '2', '6', '9', '3', '3', '7', '7', '1', '7', '8', '3', '9', '3', '7', '2', '5', '5', '8', '4', '6', '6', '1', '4', '8', '4',
    '9', '6', '8', '6', '8', '7', '8', '3', '8', '2', '8', '3', '2', '6', '0', '6', '0', '6', '0', '6', '3', '3', '8', '6', '0', '2', '4', '5', '8', '7', '7', '0', '5', '2', '8', '9', '2', '0', '7', '2', '6', '1', '7', 
    '4', '8', '1', '2', '9', '3', '9', '9', '2', '5', '2', '6', '6', '5', '6', '0', '9', '5', '7', '1', '0', '6', '1', '3', '2', '4', '9', '4', '7', '6', '5', '6', '3', '5', '0', '6', '7', '6', '3', '2', '5', '2', '3', 
    '4', '1', '2', '8', '8', '9', '9', '7', '0', '1', '0', '5', '4', '2', '3', '5', '9']
# Decrypted Bytes: [54, 49, 54, 50, 54, 51, 54, 52]
# Decrypted String: abcd




import uuid
import sys


# const unsigned char bytes[16] = {
    # 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77,
    # 0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF
# };

# will be
    # {00112233-4455-6677-8899-AABBCCDDEEFF}

# But if the encoding is little-endian, as described in SMBIOS V2.6, the same 16 bytes will represent the UUID 
    # {33221100-5544-7766-8899-AABBCCDDEEFF}


# {2F317B9D-C9E3-4D76-BFF6-B9D0D085A952}	9D 7B 31 2F E3 C9 76 4D BF F6 B9 D0 D0 85 A9 52


def le_byteorder_guid(msguid):
	""" Returns little endia guid format"""
	byteguid = ""
	byteguid += (msguid[6:8])
	byteguid += (msguid[4:6])
	byteguid += (msguid[2:4])
	byteguid += (msguid[0:2])
	
	byteguid += (msguid[11:13])
	byteguid += (msguid[9:11])
	
	byteguid += (msguid[16:18])
	byteguid += (msguid[14:16])
	
	byteguid += (msguid[19:21])
	byteguid += (msguid[21:23])
	
	byteguid += (msguid[24:])
	return byteguid;
	
	
	
	

def getguid_msguid_format(guid):
	"""returns GUI in MSGUID format"""
	msguid = ""
	msguid += (guid[7:5:-1])[::-1]
	msguid += (guid[5:3:-1])[::-1]
	msguid += (guid[3:1:-1])[::-1]
	msguid += (guid[1::-1])[::-1]
	msguid += '-'
	msguid += (guid[11:9:-1])[::-1]
	msguid += (guid[9:7:-1])[::-1]
	msguid += '-'
	msguid += (guid[15:13:-1])[::-1]
	msguid += (guid[13:11:-1])[::-1]
	msguid += '-'
	msguid += (guid[16:20])
	msguid += '-'
	msguid += (guid[20:])
	return msguid
	

if __name__ == '__main__':

	if len(sys.argv) > 1 and (sys.argv[1].lower() == "-h" or sys.argv[1].lower() == "--help"):
		print("Usage")
		print("-----------------------")
		print("python guidgen.py [OPTIONS] <RFC 4122 GUID format string to load>")
		print("\nIf no guid is provided, this will generate a new GUID in uuid version 4")
		print("\nOPTIONS")
		print("\tlittle-endian : Print guid in little endian byte order format")
		sys.exit(0);
		
	obj = None
	
	if len(sys.argv) == 3:
		obj = uuid.UUID(sys.argv[2])
	else:
		obj =  uuid.uuid4()
		
	guid = obj.urn.replace('urn:uuid:','')

	if len(sys.argv) >= 2 and sys.argv[1].lower() == "little-endian":
		guid = le_byteorder_guid(guid)
	
	print(guid)
		
	
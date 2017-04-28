from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to contine, CYRL_C to abort"

raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Allright, all done."

out_file.close()
in_file.close()



 Caused by: java.io.EOFException: \n not found: size=0 content=...
03-30 17:01:23.472 5247-7163/com.okcoin.trader W/System.err:     at com.android.okhttp.okio.RealBufferedSource.readUtf8LineStrict(RealBufferedSource.java:200)
03-30 17:01:23.472 5247-7163/com.okcoin.trader W/System.err:     at com.android.okhttp.internal.http.HttpConnection.readResponse(HttpConnection.java:191)
03-30 17:01:23.472 5247-7163/com.okcoin.trader W/System.err: 	... 9 more
#!/usr/bin/perl
use warnings;
# use lib './lib';

use CGI::Carp qw(fatalsToBrowser); # afficher les erreurs
use Time::Local;

require "./functions.pl";

print "Content-type:text/html\n\n";
print <<EndHdr;
<html><head><title>URL List</title></head>
<body>
<h2>URL List</h2>
<ul>
EndHdr
# get the file :
$filename = '/Users/juliend2/Desktop/Dropbox/perso/ressources/TEMPS/09-06-18.txt';
undef $/;
open (FILE,"< $filename") or die "Can't open $filename : $!";
my $file = <FILE>;
close(FILE);

# split the file :
%splittedfile = split(/(\n[-a-z_ ]+\s?:\n[-0-9h\s]+)/,$file); # get all the hour blobs
foreach $val (%splittedfile) { # loop into the blobs 
	if ($val =~ /([-a-z_ ]+)\s?:/i) { # get the labels
		print $1.'<br/>';	# print them 
	}
	if ($val =~ /^$/) {
		print 'hookie<br/>';
	}
	
}
pre(%splittedfile);

print <<EndFooter;
</ul>
</body>
</html>
EndFooter

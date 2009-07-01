#!/usr/bin/perl
use warnings;
# use lib './lib';

use CGI::Carp qw(fatalsToBrowser); # afficher les erreurs



require "./functions.pl";

print "Content-type:text/html\n\n";
print <<EndHdr;
<html><head><title>URL List</title></head>
<body>
<h2>Time</h2>
<ul>
EndHdr
# get the file :
$filename = '/Users/juliend2/Desktop/Dropbox/perso/ressources/TEMPS/09-06-18.txt';
undef $/;
open (FILE,"< $filename") or die "Can't open $filename : $!";
my $file = <FILE>;
close(FILE);

my ($y, $m, $d, $hh, $mm, $ss) = (localtime)[5,4,3,2,1,0]; $y += 1900; $m++;
my $iso_now = sprintf("%d-%02d-%02d %02d:%02d:%02d", $y, $m, $d, $hh, $mm, $ss);

$timeDiffStr = &timeDiff( date1 => '2009-06-28 15:36', date2 => $iso_now );
print $timeDiffStr;

# split the file :
@blocs = ();
%splittedfile = split(/(\n[-a-z_ ]+\s?:\n[-0-9h\s]+)/,$file); # get all the hour blobs
foreach $val (%splittedfile) { # loop into the blobs 
	# if ($val =~ /([-a-z_ ]+)\s?:/i) { # get the labels
	# 	print $1.'<br/>';	# print them 
	# }
	if ($val !~ /^$/) {
		push(@blocs,$val);
	}
}
# pre(@blocs);
foreach $bloc (@blocs) {
	pre($bloc);
}

print <<EndFooter;
</ul>
</body>
</html>
EndFooter

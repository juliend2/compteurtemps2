#!/usr/bin/perl
use warnings;
use CGI::Carp qw(fatalsToBrowser); # afficher les erreurs

require "./functions.pl";

print "Content-type:text/html\n\n";
print <<EndHdr;
<html><head><title>URL List</title></head>
<body>
<h2>URL List</h2>
<ul>
EndHdr

$filename = '/Users/juliend2/Desktop/Dropbox/perso/ressources/TEMPS/09-01-20.txt';
undef $/;
open (FILE,"< $filename") or die "Can't open $filename : $!";
my $file = <FILE>;
close(FILE);

%splittedfile = split(/\n/,$file);
foreach $val (%splittedfile) {
	if ($val =~ /(^[-a-z_]+)/i) {
		print $1.'<br/>';	
	}
}
pre(%splittedfile);

print <<EndFooter;
</ul>
</body>
</html>
EndFooter

#!/usr/bin/perl

sub print_r {
    package print_r;
    our $level;
    our @level_index;
    if ( ! defined $level ) { $level = 0 };
    if ( ! defined @level_index ) { $level_index[$level] = 0 };

    for ( @_ ) {
        my $element = $_;
        my $index   = $level_index[$level];

        print "\t" x $level . "[$index] => ";

        if ( ref($element) eq 'ARRAY' ) {
            my $array = $_;

            $level_index[++$level] = 0;

            print "(Array)\n";

            for ( @$array ) {
                main::print_r( $_ );
            }
            --$level if ( $level > 0 );
        } elsif ( ref($element) eq 'HASH' ) {
            my $hash = $_;

            print "(Hash)\n";

            ++$level;

            for ( keys %$hash ) {
                $level_index[$level] = $_;
                main::print_r( $$hash{$_} );
            }
        } else {
            print "$element\n";
        }

        $level_index[$level]++;
    }
} # End print_r

sub pre {
	print "<pre>";
	print_r(@_);
	print "</pre>";
}

sub timeDiff (%) {
	my %args = @_;

	my @offset_days = qw(0 31 59 90 120 151 181 212 243 273 304 334);

	my $year1  = substr($args{'date1'}, 0, 4);
	my $month1 = substr($args{'date1'}, 5, 2);
	my $day1   = substr($args{'date1'}, 8, 2);
	my $hh1    = substr($args{'date1'},11, 2) || 0;
	my $mm1    = substr($args{'date1'},14, 2) || 0;
	my $ss1    = substr($args{'date1'},17, 2) if (length($args{'date1'}) > 16);
	   $ss1  ||= 0;

	my $year2  = substr($args{'date2'}, 0, 4);
	my $month2 = substr($args{'date2'}, 5, 2);
	my $day2   = substr($args{'date2'}, 8, 2);
	my $hh2    = substr($args{'date2'},11, 2) || 0;
	my $mm2    = substr($args{'date2'},14, 2) || 0;
	my $ss2    = substr($args{'date2'},17, 2) if (length($args{'date2'}) > 16);
	   $ss2  ||= 0;

	my $total_days1 = $offset_days[$month1 - 1] + $day1 + 365 * $year1;
	my $total_days2 = $offset_days[$month2 - 1] + $day2 + 365 * $year2;
	my $days_diff   = $total_days2 - $total_days1;

	my $seconds1 = $total_days1 * 86400 + $hh1 * 3600 + $mm1 * 60 + $ss1;
	my $seconds2 = $total_days2 * 86400 + $hh2 * 3600 + $mm2 * 60 + $ss2;

	my $ssDiff = $seconds2 - $seconds1;

	my $dd     = int($ssDiff / 86400);
	my $hh     = int($ssDiff /  3600) - $dd *    24;
	my $mm     = int($ssDiff /    60) - $dd *  1440 - $hh *   60;
	my $ss     = int($ssDiff /     1) - $dd * 86400 - $hh * 3600 - $mm * 60;

	# "$dd Days $hh Hours. $mm Mins."; # returned string
	# "$hh Hours. $mm Mins."; # returned string
	$ssDiff; # seconds diff
}

sub formattime(%) {
	my %args = @_;
	my @mon = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
	printf "%s-%02d %4d", $mon[$args{'month'}], $args{'day'}, $args{'year'};
}

sub in_array {
     my ($arr,$search_for) = @_;
     return grep {$search_for eq $_} @$arr;
}

1; # sinon ca sort une erreur 500
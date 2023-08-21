BEGIN{
print " Time1\t\t Time2\t\t Difference"}
{time1=$1
time2=$2
h1=substr(time1,1,2)
m1=substr(time1,3,2)
s1=substr(time1,5,2)
h2=substr(time2,1,2)
m2=substr(time2,3,2)
s2=substr(time2,5,2)
total1 = h1*3600+m1*60+s1
total2 = h2*3600+m2*60+s2
diff =total2-total1
h_diff = int(diff/3600)
m_diff = int ((diff%3600)/60)
s_diff = int (diff%60)
formatted_diff = sprintf("%02d:%02d:%02d", h_diff, m_diff, s_diff)
formated_time1 = sprintf("%02d:%02d:%02d",h1,m1,s1)
formated_time2 = sprintf("%02d:%02d:%02d",h2,m2,s2)
    print formated_time1"\t" formated_time2"\t" formatted_diff
}

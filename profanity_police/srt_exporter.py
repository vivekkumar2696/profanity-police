import json
import math
 
class SrtExporter():
    def sec_to_hms(self, seconds):
        hours = seconds//3600
        mins = (seconds % 3600)//60
        secs = int((seconds % 3600)%60)
        print(hours, mins, secs)
        return (hours, mins, secs)

    def export(self, transcript_json, encoding = None):
        """
           
            :param file: file_path of SRT file
            :param encoding: Encoding if present
 
        """
        i = 1
        file = ''
        for data in transcript_json:
            start = data['start'] # Get start time
            stop = data['end'] # Get the end time
            content = data['text'] # Get subtitle content
            file +='{}\n'.format(i) # Add serial number
            converted_start_time = self.sec_to_hms(start)
            hour = converted_start_time[0]
            minute = converted_start_time[1]
            sec = converted_start_time[2]

            print("@", start)
            minisec = int(math.modf(start)[0] * 1000) # Processing start time
            print(minisec)
            file += str(hour).zfill(2) +':' + str(minute).zfill(2) +':' + str(sec).zfill(2) +',' + str(minisec). zfill(2) # Fill the number with 0 and write in the format

            file += ' --> '
            
            converted_stop_time = self.sec_to_hms(stop)
            hour = converted_stop_time[0]
            minute = converted_stop_time[1]
            sec = converted_stop_time[2]

            minisec = abs(int(math.modf(stop)[0] * 1000)) # Here minus 1 is to prevent two subtitles from appearing at the same time
            file += str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(sec).zfill(2) + ',' + str(minisec).zfill(2)
            file +='\n' + content +'\n\n' # add subtitle text
            i += 1

        with open('test.srt', 'w', encoding='utf-8') as f:
            f.write(file)
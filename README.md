# nextPeriod
A script to calculate time to next period, made for use on polybar

### Configuration
Script can be configured by modifying top of the python file.

```python
FORMAT = "{hours}:{minutes}"
# Use {days}, {hours}, {minutes}, {seconds}

SLEEPMSG = "zzz"
```
#### Custom Timetable
To  edit the timetable, change the values in the periods list. Each sublist represents a day, with periods[0] representing Monday, and periods[6] representing Sunday.

### Use with polybar
To use with polybar, simply create a module like the one below in your polybar config file. Then add the module to one of your bars.
```ini
[module/next-class]
type = custom/script
exec = python3 /path/to/file/nextPeriod/main.py
interval = 60
format-prefix = %{T3}祥 %{T-}
```

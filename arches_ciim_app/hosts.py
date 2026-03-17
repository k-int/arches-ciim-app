import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"arches_ciim_app"), "arches_ciim_app.urls", name="arches_ciim_app"),
)

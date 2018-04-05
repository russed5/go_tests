FROM python
RUN pip install pytest
RUN pip install requests
RUN git clone  https://github.com/russed5/go_tests/
CMD exec /bin/bash -c "pytest go_tests/service3Test.py ; sleep 2d"

cmake_minimum_required(VERSION 3.15)
project(oscillator)

file(GLOB SOURCES "*.cpp" "*.h")
add_executable(oscillator ${SOURCES})


add_executable(example)

target_sources(example PRIVATE
    main.cpp
    oscillator.cpp
    saw.cpp
    square.cpp
    sine.cpp
)
set_property(TARGET example PROPERTY CXX_STANDARD 20)

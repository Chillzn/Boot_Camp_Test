require 'test_helper'

class UsersControllerTest < ActionController::TestCase
  test "should get create" do
    get :create
    assert_response :success
  end

  test "should get redirect" do
    get :redirect
    assert_response :success
  end

  test "should get show" do
    get :show
    assert_response :success
  end

end
